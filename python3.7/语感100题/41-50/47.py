#判断字符串'this is python'是否以'this'开头，又是否以'python'结尾
a='this is python'
b=a.split(' ')
print(b[0]=='this')
print(b[-1]=='python')
