class Person:         # Python3中默认继承了object
    name='xxx'
class Animal(object):  #继承object
    name='x'

if __name__=='__main__':
    x=Person()
    print('Person',dir(x))
    y=Animal()
    print ('Animal',dir(y))
#输出结果相同 在Python3中默认继承了object
