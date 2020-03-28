year,moths=eval(input())
days=0
def Run(years):
    if (years%4==0 and years%100!=0)or year%400==0:
        print(str(years)+'是闰年，2月份是29天')
    else:
        print(str(years)+'是平年，2月份是28天')
if moths==2:
    Run(year)
elif (year%4==0 and year%100!=0)or year%400==0:
    if moths in [1,3,5,7,8,10,12]:
        days=31
        print(str(year)+'是闰年，'+str(moths)+'月份是'+str(days)+'天')
    else:
        days=30
        print(str(year)+'是闰年，'+str(moths)+'月份是'+str(days)+'天')
else:
    if moths in [1,3,5,7,8,10,12]:
        days=31
        print(str(year)+'是平年，'+str(moths)+'月份是'+str(days)+'天')
    else:
        days=30
        print(str(year)+'是平年，'+str(moths)+'月份是'+str(days)+'天')
