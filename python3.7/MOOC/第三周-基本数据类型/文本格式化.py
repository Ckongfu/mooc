import time as t

scale=50
print('执行开始'.center(60,'-'))
star=t.perf_counter()
for i in range (scale+1):
    a='*' * i
    b='.'* (scale-i)
    c=(i/scale)*100
    end=t.perf_counter()-star
    print('\r{:^3.0f}%[{}->{}]{:.2f}'.format(c,a,b,end),end='')
    t.sleep(0.1)
print()
print('执行结束'.center(60,'-'))
