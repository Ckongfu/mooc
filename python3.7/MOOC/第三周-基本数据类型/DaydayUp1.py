#DaydayUp1
import MyDay as M
'''
def dayUP(df):
    dayup=1
    for i in range(365):
        if i % 7 in[6,0]:
            dayup=(1-0.01)*dayup
        else:
            dayup=(1+df)*dayup
    return dayup
'''
dayfactory=0.001

while M(dayfactory)<37.78:
    dayfactory+=0.001
print('{:.3f}'.format(dayfactory))
