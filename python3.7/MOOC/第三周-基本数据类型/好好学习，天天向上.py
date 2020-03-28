def UP (df):
    dayup=1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
A=pow(1.01,365)
print ('A按照每天增加'+str(dayfactor)+'的能力值，在努力365天以后的能力值是：{:.2f}'.format(A))
while UP(dayfactor)<A:
    dayfactor+=0.001

print ('B在工作日的努力要比A多：{:.3f}才能在一年以后达到A的能力值'.format(dayfactor))
