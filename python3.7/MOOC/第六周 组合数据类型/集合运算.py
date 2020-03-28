A={'python',123,('python,123')}
#print(A)        #把一个集合赋值给变量A
B=set('pypy123') #把字符串按字符转换成一个集合
                #并且把相同的元素去掉
#print(B)
C={'python',123,'python',123}
#print(C)

X={1,2,3,4,5}
Y={4,5,6,7,8}
#print('X|Y',X|Y,'\n'+'X-T',X-Y,'\n'+'X&Y',X&Y,'\n'+'X^Y',X^Y)
X-=Y
print(X)
