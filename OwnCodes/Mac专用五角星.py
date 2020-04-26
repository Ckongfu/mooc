import turtle as t
t.setup(700,700,0,0)
t.color('black','red')
t.pensize(3)
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(72)
    t.forward(200)
    t.right(144)
t.end_fill()
t.hideturtle()
t.done()
