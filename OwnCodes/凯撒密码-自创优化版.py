a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a1=a.lower()
c='DEFGHIJKLMNOPQRSTUVWXYZABC'
c2=c.lower()
k=input()
for i in k:
    if i in a:
        print(c[a.index(i)],end='')
    elif i in a1:
        print(c2[a1.index(i)],end='')
    else:
        print(i,end='')

