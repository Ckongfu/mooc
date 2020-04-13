#使用map函数求列表[2,3,4,5]中每个元素的平方
def square(x):
    return pow(x,2)
a=[2,3,4,5]
b=[]
for i in a:
    x=square(i)
    b.append(x)
print(b)

'''
a=[2,3,4,5]
j=map(square,a)
print(list(j))

k=map(lambda x:pow(x,2),[2,3,4,5])
print(list(k))
'''
