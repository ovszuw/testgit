# -*- coding:UTF-8
# 作者：陈虎涛 2018-03-07
#  Python 版本：3.6.4
# 本代码实现将a.txt、b.txt二个文本文件取差集后输出c.txt文档，c.txt为a/b去除重复后的a值，输出的文档数据无序无重复。
# 将a.txt创建为列表
print ('本程序实现将a.txt、b.txt二个文本文件取差集后输出c.txt文档，c.txt为a/b去除重复后的a值，输出的文档数据无序无重复。')
print ('请确定你的Python版本不低于3.6.4，a.txt和b.txt文件已经准备就绪。')
import os
os.chdir(r'I:\jjbjcj\cj\abcjc')
lista = [] # 创建空列表lista
fa = open('A.txt',encoding='utf-8') # 打开a.txt,最后一行必须换行
# 'a.txt'每行数据赋给列表lista
for line in fa.readlines():
    lista.append(line.replace('\n','\n')) #将'\n'替换成换行

# 将b.txt创建为列表
listb = [] # 创建空列表listb
fb = open('B.txt',encoding='utf-8') # 打开a.txt,最后一行必须换行
# 'b.txt'每行数据赋给列表listb
for line in fb.readlines():
    listb.append(line.replace('\n','\n')) #将'\n'替换成换行

x = set(lista) # 将lista去重后赋给x
y = set(listb) # 将listb去重后赋给y
c = x - y # x、y取差集

fc = open('A-B.txt', 'w',encoding='utf-8') # 创建或打开'C.TXT'
fc.writelines(c) # 将交集数据写入'c.TXT'
fc.close() # 搞定，收工。

print ('正在处理数据……请稍候')
print ('搞定，打开a.txt同文件夹下的c.txt查看结果。')
input ('press enter')