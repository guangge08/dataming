#coding=utf-8
#_author_ = 'huoguang'
import re
import thread
locks = []
lock = thread.allocate_lock()

lock.acquire()
locks.append(lock)



class add(object):
    def __init__(self, m, n):
        self.a = m
        self.b = n
    def update(self, new):
        self.a = new
        print self.a

class RoundFloat():
    __slots__ = ('a', 'b')
    # def __init__(self,val):
    #     assert isinstance(val, float), "must be float!"
    #     self.value = val
def Say(**a):
    print a

if __name__ == '__main__':
    re = apply(Say, ('hello',))

    # print cls.a
    # print cls.b
    # cls.update(3)
    # print cls.__dict__.get('a')




