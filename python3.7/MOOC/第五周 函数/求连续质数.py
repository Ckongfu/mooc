def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
x=eval(input('输入一个数：'))
x1=int(x)
x1=x1+1 if x1<x else x1
count=5
while count>0:
    if is_prime(x1):
        if count >1:
            print(x1,end=',')
        else: #当count=0，也就是第五个质数的时候输出的数字后面不加','
            print(x1,end='')
        count-=1
    x1+=1
