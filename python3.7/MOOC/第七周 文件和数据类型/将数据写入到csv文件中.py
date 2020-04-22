ls=[['1,1,1'],['2,2,2'],['3,3,3'],['4,4,4']]
f=open("/Users/zouguannan/Downloads/d.txt",'w+')
for item in ls:
    f.write(','.join(item)+'\n')
f.seek(0)
print(f.read())
f.close()

