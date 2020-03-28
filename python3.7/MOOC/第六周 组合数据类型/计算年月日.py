year,moths=eval(input())
days=0
moth_days=[31,29,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year%400==0:
    days=moth_days[moths-1]
    print('{}是闰年，{}月是{}天'.format(year,moths,days))
else:
    if moths==2:
        days=moth_days[moths-1]-1
    else:
        days=moth_days[moths-1]
    print('{}是平年，{}月是{}天'.format(year,moths,days))
