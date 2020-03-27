import time
for i in range(9):
    print ('>', end='', flush=True)
    time.sleep(0.382)
print ('\nHellfire')
time.sleep(1.618)
print("地狱火导弹系统已启动!")
time.sleep(1.618)
print("目标已锁定!")
time.sleep(1.618)
for x in range(10000,-1,-1):
    mystr = "离爆炸还剩" + str(x) + "秒"
    print(mystr,end = "")
    print("\b" * (len(mystr)*2),end = "",flush=True)
    time.sleep(1)
print ('Boooooooooooooooooooooom~')
print ('任务完成！')
time.sleep(2)
input ('请确认')