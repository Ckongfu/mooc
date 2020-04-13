#返回元组(2,5,3,2,4)中元素2的个数
a=(2,5,3,2,4,2,3,2)
counts=0
for i in a:
    if i==2:
        counts+=1
    else:
        continue
print(counts)

print(a.count(2))
