#KochDrawV1

import turtle as tu
def koch(size,n):
    if n==0:
        tu.fd(size)
    else:
        for angle in [0,60,-120,60]:
            tu.left(angle)
            koch(size/3,n-1)
def main():
    tu.setup(600,600)
    tu.penup()
    tu.goto(-200,100)
    tu.pendown()
    tu.pensize(2)
    level=3 #三阶
    koch(400,level)
    tu.right(120)
    koch(400,level)
    tu.right(120)
    koch(400,level)
    tu.right(120)
    tu.hideturtle()
main()
tu.done()
