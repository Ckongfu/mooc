class Weishengwu():
    #假设一开始的老祖宗只会吃东西
    def __init__(self,name):
        self.name=name
    def eat(self):
        print ('吃东西')

class Fish(Weishengwu):
    #进化成鱼类，可以移动
    def move(self):
        print('移动')

class Houzi(Fish):
    def __init__(self,name,love):
        self.name=name
        self.love=love  #进化出一种新的属性，一种爱好：比如爱吃苹果，爱吃荡秋千等。。

    def eat(self):
        print('会用牙齿吃东西')

    def move(self):
        print ('用脚移动') #动作也进化了，都是move这个方法，以前是挪动，现在是可以用脚走路（多态）

    def Pashu(self):
        print ('爬树')
    def Now(self):
        self.eat()
        self.move()
        self.Pashu()

weishengwu=Weishengwu('weishengwu')
weishengwu.eat()
print()
Fish=Fish('fish')
Fish.move()
print()
houzi=Houzi('Houzi','apple')
houzi.Now()
print('And it can love',houzi.love)
