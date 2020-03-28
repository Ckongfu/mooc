import random
#random标准库
#random.seed(10)#随机数种子确定了随机序列的产生，可以再现随机数生成的过程
k=random.randint(1,100)#伪随机数
print(k)
#计算机不可能产生真正的随机数，所以才有所谓的伪随机数
#伪随机数：采用梅森旋转算法生成的随机序列中的元素
#基本随机函数：seed(),random()
#扩展随机函数：randint(),getrandbits(),uniform(),randrange(),choice(),shuffle()

#randint（a，b）随机一个a-b之间的随机整数
#randrange（10，100，10）生成一个10-100之间，步长为10的随机整数
#getranbits（k）生成一个长度为k比特的随机数
#uniform(a,b)在a-b之间取随机小数
print(random.uniform(0,1))#精度是小数点后16位
#choice(seq)从序列中随机选择一个元素,choices()随机取出某个元素并且返回一个列表
print (random.choice([1,2,3,4,5,6,7,8,9]))
#shuffle（seq）将序列seq中的元素随机排列，返回打乱后的序列
s=[1,2,3,4,5,6,7]
random.shuffle(s)
print(s)
b=sorted(s)
print(b)
