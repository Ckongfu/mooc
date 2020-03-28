a=int(input('Which multiplication table would you like? \n'))
b=int(input("How high do you want to go?\n"))
print ("Here's your table:")
for i in range (1,b+1):
    print (a,'X',i,'=',a*i)
