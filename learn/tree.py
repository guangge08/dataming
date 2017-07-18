#coding=utf-8
#_author_ = 'huoguang'

from math import log

def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dateSet):
    numEntries = len(dateSet)
    labelCount= {}
    for featVec in dateSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1

    shannonEnt = 0.0
    for key in labelCount:
        prob = float(labelCount[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

myDat,labels = createDataSet()
print myDat
res = calcShannonEnt(myDat)

print '当前分类的香农熵%f'%res
myDat[0][-1] = 'maybe'
print myDat
res = calcShannonEnt(myDat)
print '增加分类后的香农熵%f'%res