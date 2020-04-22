import wordcloud
txt="骂最狠的话，做最怂的人"
w=wordcloud.WordCloud(background_color='white',
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",height = 700)
w.generate(txt)
w.to_file('词云测试.png')
