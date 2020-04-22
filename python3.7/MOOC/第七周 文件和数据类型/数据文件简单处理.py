fo=open("/Users/zouguannan/Downloads/a.txt")
fo.seek(0)
str_list=fo.readlines()#读取所有行，返回一个列表
fo.close()
new_list=[]
print(str_list)
for i in str_list:
    new_list.append(i.strip('\n'))

print(new_list)
