# -*- coding: gbk -*-
import time
# localtime = time.asctime(time.localtime(time.time()))
# print ('各地市已绑定王卡助手用户计数 %s.csv' % localtime)
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# time.localtime()
time_stamp = time.strftime("%Y-%m-%d %H:%M:%S %a 时", time.localtime())
print (time_stamp)