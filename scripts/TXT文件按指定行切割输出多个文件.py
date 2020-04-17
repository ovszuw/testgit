# -*- coding:utf-8 -*-
'''
txt文件按要求的行数切割为多个txt文件，最后一个文件以实际剩余的行数为准。
'''
import os  
import time  
import os
os.chdir(r'I:\小脚本\TXT文件按指定行切割输出多个文件')
a = int(input('请输入行数：'))
def mkSubFile(lines,head,srcName,sub):  
    [des_filename, extname] = os.path.splitext(srcName)  
    filename  = des_filename + '_' + str(sub)  + extname
    print( 'make file: %s' %filename)  
    fout = open(filename,'w')  
    try:  
        fout.writelines([head])  
        fout.writelines(lines)  
        return sub + 1  
    finally:  
        fout.close()  
  
def splitByLineCount(filename,count):  
    fin = open(filename,'r')  
    try:  
        head = fin.readline()  
        buf = []  
        sub = 1  
        for line in fin:  
            buf.append(line)  
            if len(buf) == count:  
                sub = mkSubFile(buf,head,filename,sub)  
                buf = []  
        if len(buf) != 0:  
            sub = mkSubFile(buf,head,filename,sub)     
    finally:  
        fin.close()  

if __name__ == '__main__':  
    begin = time.time()  
    splitByLineCount('3月ARPU小于等于25且未订购0元包用户明细.txt',a)  # 批定目标文件及每个文件的行数
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
    input ('press enter')