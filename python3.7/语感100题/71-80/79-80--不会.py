#判断'http://blog.csdn.net'是否以'http://'或'https://'开头。若是，则返回'http'或'hppts'
a='http://blog.csdn.net'
if a[:5] in 'https://':
    print(a[:5])
else:
    print('None')
