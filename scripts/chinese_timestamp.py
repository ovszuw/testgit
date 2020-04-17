# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:44:24 2018

@author: aovs
"""

import time
time_stamp = time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime())
year = time.strftime("%Y", time.localtime())
month = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
hour = time.strftime("%H", time.localtime())
minute = time.strftime("%M", time.localtime())
second = time.strftime("%S", time.localtime())
week = time.strftime("%a", time.localtime())
week_e = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat', 'Sun')
week_c = ('星期一', '星期二', '星期三', '星期四', '星期五','星期六', '星期日')
p = week_e.index(week)
xingqi = week_c[p]
print (year + '年' + month + '月' + day + '日'+ hour + '点' + minute + '分' + \
       second + '秒' + xingqi + ' 是时')
