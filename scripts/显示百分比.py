import time
print("显示百分比")
for x in range(101):
    mystr = "百分比" + str(x) + "%"
    print(mystr,end = "")
    print("\b" * (len(mystr)*2),end = "",flush=True)
    time.sleep(0.382)
print ('完成')
time.sleep(2)
