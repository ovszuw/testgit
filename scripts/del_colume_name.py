# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:37:25 2018

@author: chenht40
"""

import pandas as pd
import time
begin = time.time()
df = pd.read_csv(r'C:\Users\chenht40\Desktop\dwtwdw.csv', header = 1, encoding = 'gbk')
target = df['电话号码']
target.to_csv('去掉列名后只包含电话号码的数据.csv', index=False, encoding = 'gbk')
end = time.time()
print ("处理完成，用时 0.0%d 秒，感谢使用~" % (end - begin))