#将字符串'2.72,5,7,3.14'以半角逗号切片后，再将各个元素转换成浮点型或整型
a='2.72,5,7,3.14'
b=a.split(',')
c=[]
d=[]
for i in b:
    i=float(i)
    c.append(i)
print(c)
for i in c:
    i=int(i)
    d.append(i)
print(d)
