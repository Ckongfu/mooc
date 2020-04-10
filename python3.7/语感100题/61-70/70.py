#将列表[0,1,2,3.14,'x','None','',list(),{5}]中的各个元素转换为布尔值
a=[0,1,2,3.14,'x',"None",'',list(),{5}]
for i in a:
    print(bool(i))
