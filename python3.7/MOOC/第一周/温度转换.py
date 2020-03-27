#TempConvert.py

TempStr=input('请输入带有符号的温度值：')
if TempStr[-1] in ['F','f'] : #索引[]，取倒数第一个字符
    C=(eval(TempStr[0:-1])-32)/1.8#eval-评估函数，取消字符串两侧的引号，返回一个数值
    print ('转换以后的温度是{:.2f}C'.format(C))#格式化---将变量C的值取2位小数，然后填充到大括号里面

elif TempStr[-1]:
    F=1.8*eval(TempStr[0:-1])+32
    print ('转换后的温度是{:.2f}F'.format(F))

else:
    print ('输入格式错误')


print(type (TempStr[0:-1]))
