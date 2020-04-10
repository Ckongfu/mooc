#将二维列表转换为一维列表
a=[[1],['a','b'],[2.3,4.5,6.7]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)
