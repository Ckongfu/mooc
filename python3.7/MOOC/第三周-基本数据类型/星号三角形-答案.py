'''
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
    '''
#其中的0，1对应format括号中的参数位置
#可以写成下面的方式：
n=eval(input())
for i in range(1,n+1,2):
    k='*'*i
    print ('{:^{}}'.format(k,n))
