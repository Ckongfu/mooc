#返回数字列表中的最大值和最小值
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a1=sorted(a,reverse=True) #按照从大到小排序
print(a1[-1])
b2=sorted(b,reverse=False) #按照从小到大排序
print(b2[-1])
