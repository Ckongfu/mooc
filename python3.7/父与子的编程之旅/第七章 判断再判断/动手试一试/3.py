a=int(input("Size of tank:"))
b=int(input("percent full:"))/100
c=int(input("km per liter:"))
d=a*b*c
print("Size of tank: ",a,'\n'+'percent full: ',b,'\n'+'km per liter:',c)
print("You can go another",d," km")
if d>200+5:
    print("The next gas station is 200 km away You can wait for the next station.")
else:
    print ('The next gas station is 200 km away '+'\n'+'Get gas now!')
