# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:39:55 2018

@author: chenht40
"""

from numpy import array
test = ['10,1,2,3,4,5,6,78']
last_test =[['10,1,2,3,4.32,5,6,7'],['10,0.625,0,0,0,0,0,0']]

def split_list(list_name):
    a = list_name[0].split(',')
    b = []
    for i in range(len(a)):
        x = float(a[i])
        b.append(x)
    return b
print (split_list(test))



finall_list = []
for item in range(len(last_test)):
    j = split_list(last_test[item])
    finall_list.append(j)
print (finall_list)
Xnew = array(finall_list)
for i in range(len(Xnew)):
    print ("X = %s" % Xnew[i][1:5])