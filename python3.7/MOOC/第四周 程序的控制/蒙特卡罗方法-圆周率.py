from random import random
from time import perf_counter
DARTS=1000*1000 #总计点数
hits=0.0 #在圆中的点
start=perf_counter()
for i in range(1,DARTS+1):
    x,y=random(),random()
    dist=pow(x**2 + y**2,0.5) #计算当前坐标离原点的距离 开根号（X平方+Y平方）
    if dist<=1.0:
        hits+=1
pi=4*(hits/DARTS)
print('圆周率值是：{}'.format(pi))
print("程序运行时间是：{:.5f}s".format(perf_counter()-start))
