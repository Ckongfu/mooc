def calculateTax(price,tax_rate):
    taxTotal=price + (price*tax_rate)
    return taxTotal
my_price=float(input('Enter a price: '))

totalPrice=calculateTax(my_price,0.06)
print ('price =',my_price,'Total price=',totalPrice)

