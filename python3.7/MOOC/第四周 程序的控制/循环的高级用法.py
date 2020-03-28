#当循环没有被break语句退出时，执行else语句快
#else语句作为完成循环的奖励

for c in 'python':
    if c =='t':
        break#continue
    print(c,end='')
else: #当else生效，即代表之前的程序代码都执行完毕了，反之，没有执行到else语句，就代表
    #前面的程序代码发生问题，或报错或是被break强制中断
    print('正常退出')
