A={'p','y',123}
try:
    while True:
        print(A.pop(),end='') #从A中不断取出元素打印出来，当没有元素取出的时候会报错
except:  #一旦报错 程序退出
    pass
