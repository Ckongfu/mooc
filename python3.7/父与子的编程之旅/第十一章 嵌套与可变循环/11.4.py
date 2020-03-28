numBlocks=int(input('How many blocks of stars do you want?'))
for block in range(1,numBlocks+1):
    for line in range(0,block*2):
        for star in range (0,(block+line)*2):
            print ('* ',end='')
        print()
    print()
