def dev(numbers,mean): #numbers是指总数列表，mean指平均数
    sdev=0.0
    for num in numbers:
        sdev+=sdev+(num-mean)**2 #求每一个数字和平均值的差的平方
    return pow(sdev/(len(numbers-1)),0.5)
