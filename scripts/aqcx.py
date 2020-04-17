# -*- coding:UTF-8
# 作者：陈虎涛 2018-03-06
#  Python 版本：3.6.4
# 本代码实现将含有重复数据的TXT文档去重后输出包含惟一值的TXT文档，每行一条数据，输出的文档数据无序。
print ('本程序实现将含有重复数据的TXT文档去重后输出包含惟一值的TXT文档，每行一条数据。')
print ('请确定你的Python版本不低于3.6.4，a.txt文件已经准备就绪。')
tip = input('确定请输入1？ ')
if tip == '1':
	lista = [] # 创建空列表lista

	fa = open( "a.txt", "r",encoding='utf-8') # 打开‘a.txt,最后一行必须换行'

# 'a.txt'每行数据赋给列表lista
	for line in fa.readlines():
		lista.append(line.replace('\n','\n')) #将'\n'替换成换行
	
	x = set(lista) # 对列表lista用set()函数进行去重，结果赋给X
	fx = open('x.txt', 'w',encoding='utf-8') # 创建或打开'X.TXT'
	fx.writelines(x) # 将不重复数据写入'X.TXT'
	fx.close() # 搞定，打开x.txt查看结果
	print ('正在处理……')
	print('搞定，打开a.txt同文件夹下的x.txt查看结果。')

else:
	print ('真调皮，不听话！')
	print('准备好了再来哦~')