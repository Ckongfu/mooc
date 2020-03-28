a=[]
b='水瓶,双鱼,白羊,金牛,双子,巨蟹,狮子,处女,天秤,天蝎,射手,摩羯'
B=b.split(',')
print(B)

for i in range(12):

    k=chr(9800+i)
    a.append(k)
y=int(input('输入你的出生月份: '))
C=B[y-1]
print(a)
print('你的星座是：{:}座'.format(C),a[y-3])

