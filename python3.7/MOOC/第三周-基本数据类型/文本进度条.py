import time as t
scale=40
print ('执行开始'.center(scale+8,'-'))
star=t.perf_counter()
for i in range(scale+1):
    a=i * '*'
    b=(scale-i) * '~'
    c=(i/scale)*100
    Time=t.perf_counter()-star
    print('\r{:.0f}%{}->{}]{:.2f}'.format(c,a,b,Time),end='')
    t.sleep(0.1)
print()
print ('执行结束'.center(scale+8,'-'))
