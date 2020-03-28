#将二维结构[['a',1],['b',2],['x',3],['y',4]]转换成字典
a=[['a',1],['b',2],['x',3],['y',4]]
b=str(a)
b.replace('[','')
b.replace(']','')
a=list(eval(b))
print(a)
