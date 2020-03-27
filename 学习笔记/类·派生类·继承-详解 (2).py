class Animal(object):    #python3.X版本中 默认加载object 在2.X版本中必须加上object
    def __init__(self,name):
        self.name=name
    def makeMoth(self):
        print (self.name+'嘴巴制作完毕')
    def makeEar(self):
        print (self.name+'耳朵制作完毕')
    def makeEye(self):
        print (self.name+'眼睛制作完毕')
    def makeHead(self):
        print (self.name+'头制作完毕')
    def makeFoot(self):
        print (self.name+'脚制作完毕')
    def makeBody(self):
        print (self.name+'身体制作完毕')
    def makeMerger(self):
        print(self.name+'合并完毕')

    def makeAll(self):
        self.makeMoth()
        self.makeEar()
        self.makeEye()
        self.makeHead()
        self.makeFoot()
        self.makeBody()
        self.makeMerger()

class Pig(Animal):   #继承了Animal的属性
                    #下面的这些属性代码可以不写，如果不写则继承Animal的属性
                    # 直接继承，
                    # 写了，继承过来的代码会被覆盖成你想要的
    def makeMoth(self):
        print (self.name+'的嘴巴制作完毕')
    def makeEar(self):
        print (self.name+'的耳朵制作完毕')
    def makeEye(self):
        print (self.name+'的眼睛制作完毕')
    def makeHead(self):
        print (self.name+'的头制作完毕')
    def makeBody(self):
        print (self.name+'的身体制作完毕')
    def makeFoot(self):
        print (self.name+'的脚制作完毕')
    def makeMerger(self):
        print (self.name+'合并完成')

    def makeAll(self):
        self.makeMoth()
        self.makeEar()
        self.makeEye()
        self.makeHead()
        self.makeBody()
        self.makeFoot()
        self.makeMerger()

class Duck(Animal):
    def makeMoth(self):
        #鸭子的耳朵很小
        print(self.name+'的耳朵制作完毕')
    def makeEar(self):
        #鸭子的眼睛也很小
        print(self.name+'的眼睛制作完成')
    def makeHead(self):
        print (self.name+'的头制作完毕')
    def makeFoot(self):
        print (self.name+'的脚制作完毕')
    def makeWing(self):
        print (self.name+'的翅膀制作完毕')

    def makeMerger(self):
        print (self.name+'合并完毕')

    def makeAll(self):
        self.makeMoth()
        self.makeEar()
        self.makeHead()
        self.makeFoot()
        self.makeMerger()
        self.makeWing()

pig=Pig('猪')
pig.makeAll()
print()
duck=Duck('鸭子')
duck.makeAll()
