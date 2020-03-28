def addInterest(balance,rate):
    newBalance=balance*(1+rate)
    balance=newBalance
   #因为没有return 默认return None
def main():
    amount=1000
    rate=0.05
    addInterest(amount,rate)
    #当这两个实参传到函数addInrerest运行,结束后并不返回任何值

    print(amount) #此处的amount就是本地定义的amount=1000
    #所以最后输出的结果其实就是本地定义的变量
main()
    #如果变量是可变对象（例如列表类型），返回到调用程序后
#该对象会呈现被修改后的状态
