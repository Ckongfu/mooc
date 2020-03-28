
import random

random.seed(10) #随机数种子确定了随机序列的产生，可以再现随机数生成的过程
for i in range(3):
    print(random.random())
#假如不给随机数种子，默认种子是第一次调用random的时间精确到微秒

