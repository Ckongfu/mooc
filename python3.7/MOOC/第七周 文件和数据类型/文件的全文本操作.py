fname=input('请输入要打开的文件名称:')
fo=open(fname,'r')
txt=fo.read(2)#读取整个文件 并保存至变量txt中
fo.close()
