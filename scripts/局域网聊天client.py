#client端实现
import socket  # 导入socket模块
sk=socket.socket()  # 实例化客户端对象
address=("SNCCHENHT40",8000)  # 设置客户端需要连接的服务端IP地址以及端口
sk.connect(address)  # 连接服务端的IP地址以及端口
while True:  # 循环实现对话
    data=input(">>>").strip()  # 获取用户输入的数据
    if data=="exit":  # 如果输入的是exit 关闭该对象并退出程序
        sk.close()  # 关闭对象
        break  # 退出循环
    sk.send(bytes(data,"utf-8"))  # 发送刚输入的数据，要先转换成bytes类型的数据
    data=str(sk.recv(1024),"utf-8")  # 接收服务端发送的数据，并将其转换成unicode数据类型
    print("-->",data)  # 打印服务端传输过来的数据