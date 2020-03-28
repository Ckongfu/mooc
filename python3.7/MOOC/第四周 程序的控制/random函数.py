import random

print(random.randint(1,10)) #随机一个范围以内的整数
print(random.random())      #随机一个0-1以内的浮点数
print(random.uniform(1,5))  #随机一个范围以内的浮点数
print(random.choice('Hello World!')) #从一个序列中随机选取一个元素
print(type(random.choice('Hello World!')))#随机选取一个元素，返回类型和原序列相同
print(random.randrange(2,100,2))#按步长随机选取一个范围内的元素（可以用来选奇偶数）

a=[1,2,3,4,5]
random.shuffle(a) #打乱列表重新排序
print(a)
