text=open("/Users/zouguannan/Downloads/a.txt")
text=text.readlines()
#text.write('中国是一个伟大的国家！\n')
text1=[]
#text.seek(0)#设定指针的位置
'''
ls=['中国','法国','美国','\n']
text.writelines(ls)#writelines()将列表的元素拼接以后写入文件中
'''
for i in text:
    i=i.replace('\n','')
    text1.append(i)
print(text1)
#text.close()

