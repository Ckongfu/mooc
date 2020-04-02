#将列表[3,0,8,5,7]中大于5的元素设置为1，其余设置为0
a=[3,0,8,5,7]
b=[]
for i in a:
    if i<=5:
        i=0
    else:
        i=1
    b.append(i)
print(b)
