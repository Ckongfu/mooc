f=open('/Users/zouguannan/Downloads/a.txt','a+')
ls=['中国','美国','法国','\n']
f.write('*'.join(ls))
f.seek(0)
print(f.read())
f.close()
