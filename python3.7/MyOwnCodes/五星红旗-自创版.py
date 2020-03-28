import turtle as t
t.hideturtle()
def pentagram(a):
    t.color('yellow')
    t.begin_fill()
    for i in range (5):

        t.fd(a)
        t.right(144)
        t.fd(a)
    t.hideturtle()
    t.end_fill()
t.penup()
t.goto((-300,300))
t.pendown()
t.color('red')
t.begin_fill()
for i in range(2):
    t.fd(600)
    t.right(90)
    t.fd(400)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-200,180)
t.pendown()
pentagram(60)
k=60
for i in range(1,5):
    t.seth(72-i*18)
    t.penup()
    t.goto(-190,30)
    t.seth(0)
    t.circle(130,k)
    t.pendown()
    pentagram(20)
    t.penup()
    k+=23.33

t.done()
