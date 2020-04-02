#返回元组(2,5,3,2,4)中元素2的个数
a=(2,5,3,2,4)
count=0
for i in a:
    if i==2:
        count+=1
    else:
        continue
print(count)

