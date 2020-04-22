import jieba
import wordcloud
from imageio import imread
mask=imread("zhong.png")
f=open("/Users/zouguannan/Downloads/f.txt",'r',encoding='utf-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(font_path="/System/Library/Fonts/STHeiti Medium.ttc",
                      width=1000,height=700,background_color='white',mask=mask,
                      max_words=25)
w.generate(txt)
w.to_file('乡村振兴战略2.png')
