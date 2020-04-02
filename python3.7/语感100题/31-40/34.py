#返回在元组(2,5,3,7)索引号为2的位置插入元素9之后的新元组
a=(2,5,3,7)
b=list(a)
b.insert(2,9)
print(tuple(b))

