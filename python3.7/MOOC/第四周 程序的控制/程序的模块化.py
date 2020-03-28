def createTable(principal,apr):
    #为每一年绘制星号的增长图
    for year in range(1,11):
        printcipal=printcipal*(1+apr)
        print('{}d'.format(year),end='')
        total=caculateNum(principal)
        print('*'* total)
    print('0.0k     2.5k    5.0k    7.5k    10.0k')

def caculateNum(principal):
    #计算星号数量
    total=int(principal*4/1000.0)
    return total

def main():
    print('This program plots the growth of a 10-year investment.')
    principal=eval(input('Enter the initial principal: '))
    apr=eval(input('Enter the annualized interest rate: '))
    createTable(principal,apr)
main()
