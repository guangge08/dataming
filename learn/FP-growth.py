#coding=utf-8
#_author_ = 'huoguang'
from numpy import *


class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print '  '*ind, self.name, ' ', self.count
        for child in self.children.values():
            child.disp(ind+1)

if __name__   == "__main__":
    # rootNode = treeNode('pyramid', 9, None)
    # rootNode.children['eye'] = treeNode('eye', 13, None)
    # rootNode.children['ear'] = treeNode('ear', 9, None)
    # rootNode.children['ear'].children['num'] = treeNode('num', 1, None)
    # rootNode.disp()
    a = [['a', 'b', 'c'], ['d']]
    b = frozenset('abcde')
    print b
    for trans in b:
        print b[trans]













