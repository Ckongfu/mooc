#写一个函数，以0.1秒的间隔不换行打印30次由函数参数传入的字符，实现类似打字机的效果
import time
def prints(words):
    if words:
        for i in range(3):
            print(words *3,end='')
            time.sleep(0.5)
a=input('请输入你要打印的字符:')
prints(a)
