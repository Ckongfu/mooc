import wordcloud
from imageio import imread
txt=open("/Users/zouguannan/Downloads/1.txt")
f=txt.read()
mk=imread("/Users/zouguannan/Downloads/xx.jpg")
w=wordcloud.WordCloud(background_color='white',
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
mask=mk,
width=400,height = 700)
w.generate(f)
w.to_file('词云测试.png')
