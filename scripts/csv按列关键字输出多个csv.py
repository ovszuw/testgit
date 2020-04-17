# -*- coding: utf-8 -*-  
""" 
将CSV文件按某列的关键字切割输出以关键字命名的CSV文件，支持中文字符。
python版本：3.6.4
需安装Panads
实测227万条CSV数据，按列关键字分为10个CSV文件用时约3秒。
"""  
import pandas as pd # 导入pandas库。
f = pd.read_csv('test2.csv', encoding='gbk')  # 读取目标CSV文件，示例文件'test1.csv'。
groups = f.groupby(f[u'地市'])  # 需要按列切割的列名
# 按列关键字进行切割输出。
for group in groups:  
  group[1].to_csv(str(group[0]) + '.csv', index=False, encoding='gbk') 

print ("按列关键字分CSV完毕，请到同文件夹下查看输出的文件")