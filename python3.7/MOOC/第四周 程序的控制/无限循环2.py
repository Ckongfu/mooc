s='python'
'''
while s !='':
    for c  in s:
        print(c,end='')
    s=s[:-1]
'''
while s !='':
    for c  in s:
        if c=='t':
            break #多层循环时，break只跳出当次、当层循环，外部循环继续
        print(c,end='')
    s=s[:-1]
