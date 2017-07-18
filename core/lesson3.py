#coding=utf-8
#_author_ = 'huoguang'

import types
import string
"如果模块被导入，__name__值为模块名字。 如果模块式被直接执行，__name__的值为'__main__'"
if __name__   == "__main__":
    # list = [1,2,3,3,8]
    # list.reverse()
    # print list.count(3)
    # list.pop()
    # a = "abc"
    #
    # # list.append("a")
    # #
    # # print enumerate(list)
    # # for i in enumerate(list):
    # #     print i
    # c = ('a','b','c')
    # d = {}.fromkeys(c)
    # e = dict(x=1,y=2)
    # print e.setdefault('g',4)
    a = 1
    # while (a < 10):
    #     print "index is: ", a
    #     a += 1
    #     if (a == 5):
    #         break
    #
    # else:
    #     print"finish"
    file = open('text.txt','r')
    print type(file)


