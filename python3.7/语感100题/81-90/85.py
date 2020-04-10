#将两个等长的列表转换为字典
a=['a','b','c','d']
b=[1,2,3,4]
c=dict(map(lambda x,y:[x,y],a,b))
print(c)
