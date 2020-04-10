#判断字符串'adS12K56'是否完全为字母数字，是否全为数字，是否全为字母，是否全为ASCII码
a='adS12K56'
print(a.isdigit()) #判断字符串是否为数字类型
print(a.isascii()) #判断字符串是否为ASCII
print(a.isalpha()) #判断字符串是否为字母
print(a.isalnum()) #判断字符串是否为字母+数字组成
