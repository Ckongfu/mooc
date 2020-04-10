#输出列表[8,5,2,4,3,6,5,5,1,4,5]中出现最频繁的数字 以及出现的次数
a=[8,5,2,4,3,6,5,5,1,4,5]
b={}
for  i in a:
    b[i]=a.count(i)#把所有的数字和出现的次数写成一个字典
print(b)
max_val=max(b.values())
c=dict([val,key] for key,val in b.items())
print('出现最多的数字是:',c[max_val],',出现的次数是',max_val,'次')
