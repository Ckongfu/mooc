def num():
    count = 0   #定义输入次数的起始值
    for i in range(3):  #限定输入错误次数为3次，第三次错误程序退出
        Input= eval(input("请输入一个数字（1-12）之间："))
        if 1<=Input<=12:
            return Input    #如果用户输入的数值在1-12之间，就函数就返回用户的输入值，函数结束运行
        else:
            count += 1
            if count==3:    #假如输入次数等于三次的时候提示
                print('输入次数过多，程序退出！')
            else:
                print("输入错误!",'你还有',3-count,'次机会')  #如果输入值不在1-12之间提示输入错误，并且进行下一次循环
try:
    x = num()
    print(x + 100)
except:
    pass
