a=3
while a>0:
    a=a-1     #假如a=a+1则结果和条件成立，语句会永远执行
    print(a)

for c in 'pthon':
    if c=='t':
        continue #当continue生效时，此次过程到此结束，进行下次循环
    print(c,end='')

for c in 'python':
    if c=='t':
        break #当条件满足执行break时，整个程序到此结束
    print(c,end='')

