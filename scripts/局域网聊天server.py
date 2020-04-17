#server端实现:
import socket  # 导入socket模块
sk=socket.socket()  # 实例化socket对象
address=("SNCCHENHT40",8000)  # 定义好监听的IP地址和端口，可以绑定网卡上的IP地址，但是生产环境中一般绑定0.0.0.0这样所有网卡上都能够接收并处理这个端口的数据了
sk.bind(address)  # 绑定IP地址和端口
sk.listen(5)  # 设定侦听开始并设定侦听队列里面等待的连接数最大为5

while True:  # 循环，为了建立客户端连接
    conn,addr=sk.accept()  # conn拿到的是接入的客户端的对象，之后服务端和客户端通信都是基于这个conn对象进行通信，add获取的是连接的客户端的IP和端口
    while True:  # 这个循环来实现相互之间聊天的逻辑
        try:  # 为什么要使用try包裹这一块呢？因为在通信过程中客户端突然退出了的话，服务端阻塞在recv状态时将会抛出异常并终止程序，为了解决这个异常，需要我们自己捕获这个异常，这是在windows上，linux上不会抛出异常
            data=conn.recv(1024)  # 定义接收的数据大小为1024个字节并接受客户端传递过来的数据，注意这里的数据在python3中是bytes类型的，在python3中网络通信发送和接收的数据必须是bytes类型的，否则会报错
            if data:  # 假如客户端传递数据过来时
                print("-->",str(data,"utf-8"))  # 打印客户端传递过来的数据，需要从bytes类型数据解码成unicode类型的数据
                data=bytes(input(">>>"),"utf-8")  # 接收输入的数据并转换成bytes类型的数据
                conn.send(data)  # 将bytes类型的数据发送给客户端
            else:  # 否则关闭这个客户端连接的对象，当客户端正常退出，执行了sk.close()时将不会发送数据到服务端，也就是说recv获取到的数据是空的
                conn.close()  # 这时关闭这个conn对象并退出当前循环等待下一个客户端对象来连接
                break
        except ConnectionResetError as e:  # 捕获到异常之后，打印异常出来并退出循环等待下一个客户端连接
            print(e)
            break