#coding=utf-8
#_author_ = 'huoguang'
from numpy import *

def loadData():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [1, 1, 1, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1]]

if __name__   == "__main__":
    Data = loadData()
    U, Sigma, VT = linalg.svd(Data)

    Sig3 = mat([[Sigma[0], 0, 0], [0, Sigma[1], 0], [0, 0, Sigma[2]]])
    res = U[:, :3]*Sig3*VT[:3, :]
    print res







