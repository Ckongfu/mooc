a=[]
for z in range(10):
    for y in range(10):
        for x in range(1,10):
            k=eval(str(x)+str(y)+str(z))
            if 99<k<1000 and k==x**3+y**3+z**3:
                a.append(k)
k=''
for i in a:
    k+=str(i)+','
print(k+'\b')
