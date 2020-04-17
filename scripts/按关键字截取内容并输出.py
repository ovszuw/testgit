# __*__ coding: utf-8 __*__
'''
按关键字截取TXT文件关键字中间包含的内容并输出TXT文件。
截取的内容必须位于关键字中间
关键字必须成对，且必须一样。
'''
import re
import linecache
 
def fileParse():
    inputfile = input('Input SourcFile:') ##输入源文件，如A.txt
    fp = open(inputfile, 'r')
 
    number =[]
    lineNumber = 1
    keyword = input('Slice Keyword:') ##输入你要切分的关键字
    outfilename = input('Outfilename:')##输出文件名，如out.txt则写out即可，后续输出的文件是out0.txt,out1.txt...
 
    for eachLine in fp:       
        m = re.search(keyword, eachLine) ##查询关键字
        if m is not None:
           number.append(lineNumber) #将关键字的行号记录在number中
        lineNumber = lineNumber + 1
    size = int(len(number))
    for i in range(0,size-1):
        start = number[i]
        end = number[i+1]
        destLines = linecache.getlines(inputfile)[start:end-1] #将行号为start+1到end-1的文件内容截取出来
        fp_w = open(outfilename + str(i)+'.txt','w') #将截取出的内容保存在输出文件中
        for key in destLines:
            fp_w.write(key)
        fp_w.close()
 
if __name__ == "__main__":
    fileParse()