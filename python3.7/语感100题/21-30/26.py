#若a=dict(),令b=a，执行b.update({'x':1})，a亦被改变，为何？如何避免
a=dict()
b=dict(a) #b=a是指给字典多加了一个名为b的标签，b=dict(a)建立一个新的字典b
a.update({'x':1})
print( 'a=',a,'\nb=',b)
