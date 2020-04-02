#以列表形式返回字典{'Alice':20,'Beth':18,'Cecil':21}中的所有值
a={'Alice':20,'Beth':18,'Cecil':21}
b=list(a.keys())    #输出所有键
c=list(a.values())  #输出字典的所有值
print(b+c)
