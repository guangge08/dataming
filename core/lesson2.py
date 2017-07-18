#coding=utf-8
#_author_ = 'huoguang'
# a = "aaa"
# print "%s and %d" % (a, 1)
# dic = {}
# dic["a"] = "b"
# print dic["a"],
# flag = 3
# if flag == 0:
#     print 1
# elif flag == 1:
#     print 2
# else:
#     print f
import io
import os

def foo():
    str = 'This is a big stuck'
    return [a.lower() for a in str.split(' ') if len(a) > 1]

if __name__ == "__main__":
    print ("Hello Python !!")



    # fname = 'text.txt'
    # # fname = raw_input('enter please: ')
    # os.chdir('./')
    # print os.getcwd()
    # os.chdir('example')
    #
    # try:
    #     fobj = open(fname, 'r')
    # except IOError, e:
    #     print "*** file open error:", e
    # else:
    #     for line in fobj:
    #         print line
    #     fobj.close()