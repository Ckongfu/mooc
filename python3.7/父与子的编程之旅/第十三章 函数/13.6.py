def calculateTax(price,tax_rate):
    total=price+(price*tax_rate) #total为局部变量
    print(my_price)
    return total
my_price=float(input('Enter a price: '))#my_price为全局变量
totalPrice=calculateTax(my_price,0.06)
print('price=',my_price,'Total price =',totalPrice)
