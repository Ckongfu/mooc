#非等位移动-凯撒密码
dict_all="ABCDEFGHIJKLMNOPQRSTUVWXYZ"#建立一个包含所有字母的密码本
Input=(input(''))
Input=Input.upper()  #将用户输入格式化成大写
counts=0 #用户输入的字符计数
News=''#最后生成的密码
for i in Input:
    counts+=1#每遍历一个元素就记录元素的位置
    if i in dict_all: #
        try:#防止超出密码本的长度
            News+=dict_all[dict_all.index(i)+counts]
        except:
            News += (dict_all*counts)[(dict_all*counts).index(i) + counts]#假如元素的位置超出密码本的长度就把密码本复制延长
    else:
        News+=i#如果元素不在密码本中 就输出元素本身
print(News)
