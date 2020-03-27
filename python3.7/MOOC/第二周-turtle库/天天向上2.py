#DaydayUp2
dayfactory=0.005
dayup=pow(1+dayfactory,365)
daydown=pow(1-dayfactory,365)
print('向上:{:.2f},向下:{:.2f}'.format(dayup,daydown))
