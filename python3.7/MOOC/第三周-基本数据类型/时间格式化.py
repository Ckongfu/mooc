import time

print(time.strftime('%Y-%m-%d %H:%M:%S'))

print(time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))

print(time.gmtime())
print(time.ctime())

timestr='2020-03-03 21:38:22'

print(time.strptime(timestr,'%Y-%m-%d %H:%M:%S'))
#time.strptime()函数是讲字符串形式的日期转换成
# 计算机能读取的时间格式(即:time.gmtime())
#time.strftime()是将计算机能读取的时间格式转换成人类易读的格式
