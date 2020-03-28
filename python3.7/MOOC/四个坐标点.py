import turtle as t

t.penup()
t.pensize(5)
t.colormode(255)
t.pencolor(255,175,203)
t.goto(100,100)
t.pendown()
t.goto(100,-100)
t.goto(-100,-100)
t.goto(-100,100)
t.goto(100,100)
t.penup()
t.goto(0,0)
t.pendown()
t.fd(-200)
t.fd(400)
t.goto(0,0)
t.goto(0,200)
t.goto(0,-200)
#t.hideturtle() #隐藏海龟图标

t.done()
