#CalStaticsV1
def getNum(): #获取用户的输入列表
    nums=[]
    iNumStr=input('请输入数字（exit退出）：')
    while iNumStr!='exit':
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字（exit退出）：")
    return nums
def mean(numbers): #计算平均值
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)
def median(numbers): #计算中位数
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
def dev(numbers,mean): #numbers是指总数列表，mean指平均数
    sdev=0.0
    for num in numbers:
        sdev+=sdev+(num-mean)**2 #求每一个数字和平均值的差的平方
    return pow(sdev/(len(numbers-1)),0.5)
n=getNum()
m=mean(n)
print(n,m)
