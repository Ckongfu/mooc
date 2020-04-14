list_a=[True,1,0,'x',None,'x',False,2,True]
print(type(list(list_a.remove('x') for i in list_a if i=='x')))
li=[x for x in range(1,11) if x==8]
print(li)
