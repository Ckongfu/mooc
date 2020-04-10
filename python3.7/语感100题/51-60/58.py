#将三个字符串'15','127','65535'左侧补零成同样的长度
a='15'
b='127'
c='65535'
print(a.rjust(len(c),'0'))
print(b.rjust(len(c),'0'))
print(c)
