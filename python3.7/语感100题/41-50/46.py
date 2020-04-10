#饭就字符串'this is python'首字母大写以及字符串内每个单词首字母大写形式
import re
a='this is python'
b=a[0]
print(b.upper()+a[1:])
print(a.split(' ')) #按某个字符进行切片，并且返回一个列表
