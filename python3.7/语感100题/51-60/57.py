#将三个全英文字符串（比如:，'Hello,我是David','OK',好,'很高兴认识你')分行打印，实现左对齐、右对齐和剧中对齐效果
a='Hello,我是David'
b='OK,好'
c='很高兴认识你'
print('{}\n{}\n{}'.format(a,b,c))
print(a.center(30))
print(b.ljust(30))
print(c.rjust(30))
