a=int(input('输入一个奇数：'))
for i in range(a//2+1):
    i=i*2+1
    print(('*'*i).center(a,' '))
