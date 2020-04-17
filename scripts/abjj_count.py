# -*- coding:UTF-8
# 作者：陈虎涛 2018-03-07
#  Python 版本：3.6.4
# 本代码实现将a.txt、b.txt二个文本文件取交集后输出c.txt文档，输出的文档数据无序。
# 将a.txt创建为列表
import time
begin = time.time()

print ('本程序实现王卡助手群发效果统计功能。')
# print ('请确定你的Python版本不低于3.6.4，a.txt（群发前未绑定目标用户）和b.txt（群发后未绑定目标用户）文件已经准备就绪。')

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
c = x & y # x、y取交集

a = len(lista)
b = len(c)
d = a - b
print ("正在统计请稍候……")
print ("群发前目标用户未绑定数量为: %d" % (a))
print ("群发后目标用户未绑定数量为: %d" % (b))
print ("群发后目标用户绑定数为: %d"  % (d))
end = time.time()
print ("用时 0.0%d 秒，感谢使用~" % (end - begin))

