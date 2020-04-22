import jieba

jieba.add_word('真武七截阵')
jieba.add_word('天罡北斗阵')
list1=jieba.lcut('真武七截阵和天罡北斗阵哪个更厉害呢？')
for i in list1:
    print(i,end=',')

