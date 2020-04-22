a='中国是一个伟大的国家'
print(a.encode(encoding='utf-8'))
print(a.encode(encoding='utf-8').decode(encoding='utf-8'))
f=open('f.txt') #文本形式、只读模式、默认值
f=open('f.txt','rt')#文本形式 只读模式 （和默认值相同）
f=open('f,txt','w') #文本形式、覆盖写模式
f=open('f.txt','a+') #文本形式、追加写模式+读文件
f=open('f.txt',a)#文本形式，仅写入信息
f=open('f.txt','x') #文本信息，创建写模式
f=open('f.txt','b')#二进制形式、只读模式
f=open('f.txt','wb')#二进制模式，覆盖写模式
f.close() #关闭文件
