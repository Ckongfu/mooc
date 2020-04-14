for j in range (1,10):
    for i in range(1,10):
        if j<=i:
            print('%d*%d=%-5d'%(j,i,j*i),end='')
    print()
