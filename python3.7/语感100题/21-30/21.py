#以列表形式返回字典{'Alice':20,'Beth':18,'Cecil':21}中的所有键值，返回元组
a={'Alice':20,'Beth':18,'Cecil':21}
b=list(a.keys())    #输出所有键
c=list(a.values())  #输出字典的所有值
k=[]
b1=len(b)
c1=len(c)
while b1>0:
    tuple=b[b1-1],c[c1-1]
    b1-=1
    c1-=1
    k.append(tuple)
print(sorted(k))

