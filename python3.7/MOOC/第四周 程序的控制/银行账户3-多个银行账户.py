def addInterest(balance,rate):
    for i in range(len(balance)):
        balance[i]=balance[i]*(1+rate)

def test():
    amounts=[1000,105,3500,739]
    rate=0.05
    addInterest(amounts,rate)
    print(amounts)
    #函数的参数是通过值来传递的
    #如果变量是可变对象（例如列表类型），返回到调用程序后
#该对象会呈现被修改后的状态
test()
