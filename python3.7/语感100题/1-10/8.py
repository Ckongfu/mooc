#删除列表中的索引号为奇数或者偶数的元素
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(0,len(a),2):
    b.append(a[i]) #建立一个列表
print(set(a)-set(b)) #将两个列表转换成集合进行差集运算得出奇数元素，最后再转换成列表
print(b)
#del a[::2]
#print(a)
