def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
list1=[]
for i in range(1,101):
    if prime(i):
        list1.append(i)
    else:
        continue
print('100以内的素数是',list1)
