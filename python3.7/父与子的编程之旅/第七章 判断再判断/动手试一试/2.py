sex=input("What is your sex,'m'or'f': ")
age=0
if sex=='m':
    print ('Sorry we only need girls!')
elif sex=='f':
    age=int(input('In put your age: '))
    if 10<=age<=12:
        print('OK!!!')
    else:
        print('Sorry your age is not nessary!!')
else:
    print ('Enter error!!!')
