#将元组（1，2，3）和集合{4，5，6}合并成一个列表
a=(1,2,3)
b={4,5,6}
ls=list(a)+list(b) #分别将元组a和集合b转换成一个列表副本，然后相加
print(ls)
