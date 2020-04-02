#从列表[True,1,0,'x',None,'x',False,2,True]
a=[True,1,0,'x',None,'x',False,2,True]
while 'x' in a: #判断只要列表a中有'x'元素，就执行a.remove('x')
    a.remove('x')
print(a)

