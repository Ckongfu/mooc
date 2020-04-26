dict_all="ABCDEFGHIJKLMNOPQRSTUVWXYZ"#建立一个包含所有字母的密码本
Input=(input('')).upper()
counts=0 #用户输入的字符计数
News=''#建立一个最后生成的密码变量
for i in Input:
    counts+=1#每遍历一个元素就记录该元素的位置
    if i in dict_all:
        News += (dict_all*counts)[dict_all.index(i) + counts]
        #1.使用index函数确定元素在只有一个密码本的相对位置
        #2.得到元素的相对位置以后，加上counts，表示元素的绝对位置
        #3.元素的位置序号每增加1，密码本的长度就增加一倍。这样就不会出现元素的位置数值，大于密码本的长度(此处投机取巧)
    else:
        News+=i#如果元素不在密码本中 就输出元素本身
print(News)
