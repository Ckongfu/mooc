y,moths = eval(input())
leap='平'
moth_days = [31,28,31,30,31,30,31,31,30,31,30,31]
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
    moth_days[1] = 29
    leap='闰'
days = moth_days[moths-1]
print("{}年是{}年,{}月有{}天".format(y,leap,moths,days))
