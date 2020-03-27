
a= eval(input())
for i in range(1,a+1,2):
    b='*'*i
    print("{0:^{1}}".format(b,a))
