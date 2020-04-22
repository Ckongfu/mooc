def median(numbers):#计算中位数
    numbers=sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
a=[1,3,9,4,8,5,6,7,2]
x=median(a)
print(x)
