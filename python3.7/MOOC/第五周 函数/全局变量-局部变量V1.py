ls=["F","f"]
def func (a):
    #ls=[] 当函数内部没有创建这个变量时，默认就是全局变量。
    #当创建这个变量时，这个变量就是函数内部创建的局部变量
    # 即使名称和全局变量相同也是不同的两个变量
    ls.append(a)
    return ls

func('c')
print (ls)
