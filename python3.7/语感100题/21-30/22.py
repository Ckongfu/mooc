#像字典{'Alice':20,'Beth':18,'Cecil':21}中追加'David':19,更新Cecil的值为17
a={'Alice':20,'Beth':18,'Cecil':21}
a['Cecil']=17
b={'David':19}
a.update(b)
print(a)
