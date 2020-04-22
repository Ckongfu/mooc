fo=open("/Users/zouguannan/Downloads/a.txt",'a+')
ls=["中国","法国","美国",'\n']
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
