f=open('/Users/zouguannan/Downloads/1.txt')
#s=f.read(2) #指定参数后 读取前x个字符
#s=f.readline(6)#读取一行中的前6个人元素
s=f.readlines(2) #读取10行,若没有指定 则读取所有行
f.seek(0)
f.close()
print(s)
