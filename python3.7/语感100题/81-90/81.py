#将列表[2,'a',5.2,4,{},9,[]]中大于3的整数或者浮点数置为1，其余置为0
a=[3,'a',5.2,4,'{}',9,'[]']
b=[]
for i in a:
    x=type(i)
    if x in [int,float]:#if x== int or x==float
        if 3<i:
            i=1
            b.append(i)
        else:
            i=0
            b.append(i)
    else:
        i=0
        b.append(i)
print(a)
print(b)
c=dict(map(lambda x,y:[x,y],a,b))
print(c)
