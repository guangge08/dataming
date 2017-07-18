#coding=utf-8
#_author_ = 'huoguang'
# import os.path
# import sys
from numpy import *
fr = open('F:\\pythontest.txt','r')
arrayOLines = fr.readlines()
# print '!!!',arrayOLines
num = len(arrayOLines)
returnMat = zeros((num,3))
classLabelVector = []
index = 0
for line in arrayOLines:
    line.strip()
    listF = line.split('\t')
    returnMat[index,:] = listF[0:3]
    print "!!!",int(listF[-1])
    classLabelVector.append(int(listF[-1]))
    index +=1

print returnMat

print classLabelVector

