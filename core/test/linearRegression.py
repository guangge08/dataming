#coding=utf-8
#_author_ = 'huoguang'
import sklearn

def loadData(filename):
    """从文件读取数据"""
    numFeat = len(open(filename).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(lineArr[-1])
    return dataMat, labelMat

def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0:
        print "cannot do inverse"
        return
    ws = xTx.I*(xMat.T*yMat)
    return ws




if __name__ == '__main__':
    loadData('a')
    print 'Finish !!'