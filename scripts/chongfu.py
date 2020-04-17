list = ['0','1','2','2','3','3','3','4','4','4','4']
a = []
for i in list:
  if list.count(i) > 1:
    a.append(i)
lista = set(a)
c = []
for x in lista:
    j = list.count(x)
    c.append('%s 重复了 %s 次' % (x, j) + '\n')
with open ('result.txt', 'w') as re:
    re.writelines(c)