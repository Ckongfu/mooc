#平均数、排序
nums=input()
nums=nums.split(' ')#把用户输入的数字 按照空格切片，返回一个列表（此列表中的所有元素为字符串）
nums_list=[]#这个新列表将放入的元素为数值
sum=0
times=0
for i in nums:
    nums_list.append(eval(i))#把格式化为数值的数字，加入到新列表
    sum+=eval(i)#计算用户输入数字的总和
    times+=1#计算用户一共输入了多少数字
nums_list.sort(reverse=True)#按从大到小排序
print('{:.2f}\n{} {} {}'.format((sum/times),nums_list[0],nums_list[1],nums_list[2])) #取排序后的前三个值
