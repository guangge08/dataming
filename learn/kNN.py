#coding=utf-8
#_author_ = 'huoguang'
#kNN 分类器

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classif0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # print dataSetSize
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # print diffMat
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    print classCount
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
res = classif0([1.2,1.1], group, labels, 3)
print "输入的元素归类于",res,"!!"