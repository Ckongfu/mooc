#从键盘输入年月日时分秒，输出形如'2019-05-01 12：00：00'的字符串
a=input()
print('{}-{}-{} {}:{}:{}'.format(a[0:4],a[4:6],a[6:8],a[8:10],a[10:12],a[12:]))

