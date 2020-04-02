#以列表["A","B","C","D","E","F","G"]中的每一个元素为键，默认值都0为值，创建一个字典
a=["A","B","C","D","E","F","G"]
b=[1,2,3,4,5,6,7]
k={}
x=0
for i in range(0,len(a)):
    k[a[i]]=b[x]
    x+=1
print(k)
'''
c=dict(map(lambda x,y:[x,y] , a,b))
print(c)
print({k:v for k,v in zip(a,b)})
'''
