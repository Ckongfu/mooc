a=eval(input())

b=str(pow(a,3))
c=b.center(20,'-')

if len(b)<=20:
    print(c)
else:
    print(b)

