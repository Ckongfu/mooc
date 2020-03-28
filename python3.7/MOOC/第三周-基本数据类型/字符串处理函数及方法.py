print('1+1=2',chr(10004))
print('这个字符️♉的Unicode值是：'+str(ord('♉')))
print(chr(9801))
for i in range(12):
    print(chr(9801+i),end=' ')

print()
str='A,C,D,E,F,A,B,C,C,C,C,G'
#print(str.split(',',2))#参数2是指分割两次

print(str.count('A'))

str.replace('C','222')
print(str)

print('python'.center(20,'=') )     #将字符串放在中间，左右以'='填充，总计50个字符

print('{:=^20}'.format('python'))

