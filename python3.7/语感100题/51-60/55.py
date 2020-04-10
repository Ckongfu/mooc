#清除字符串'\t pytho \n'左侧、右侧，以及左右两侧的空白字符
a='\t python \n'
print(a.lstrip('\t')) #删除左侧字符
b=a.lstrip('\t')
print(b.rstrip(('\n'))) #删除右侧字符串

c='aaa123bbb'
print(c.lstrip('a'))
print(c.rstrip('b'))
print(c.strip('ab'))
