fo=open("/Users/zouguannan/Downloads/c.txt")
ls=[]
for line in fo:
    line=line.replace('\n','')
    ls.append(line.split(','))
print(ls)
fo.close()
