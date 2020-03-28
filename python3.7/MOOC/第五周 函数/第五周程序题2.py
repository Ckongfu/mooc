def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
list1=[]
k=eval(input())
for i in range(k,k+6):
    if prime(i):
        list1.append(i)
    else:
        continue
print(list1)
