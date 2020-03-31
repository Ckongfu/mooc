import jieba
s='工信处干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'
for i in jieba.cut(s):
    print(i,end=',')

s=jieba.lcut(s,cut_all=True)   #全模式
print(s)
i='中华人民共和国是伟大的'
ls1=jieba.lcut_for_search(i) #搜索引擎模式
print(ls1)

