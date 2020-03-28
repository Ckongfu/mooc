money=float(input("How much do you buy:"))
pay=0

if money<=10:
    pay=(1-0.1)*money
    print('You will paid',pay)
if money>10:
    pay=(1-0.2)*money
    print('You will paid',pay)
