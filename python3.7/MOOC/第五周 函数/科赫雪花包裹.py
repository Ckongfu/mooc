import turtle as tu

def coch(size,n):
    if n==0:
        tu.fd(size)
    else:
        for i in [0,60,-120,60]:
            tu.left(i)
            coch(size/3,n-1)
def main():
    tu.setup(800,800)
    tu.penup()
    tu.goto(-300,100)
    tu.pendown()
    tu.pensize(2)
    level=3
    coch(600,level)
    tu.right(120)       #执行完一次画线以后海龟旋转120度，
                        # 旋转3次就合成了一个雪花
    coch(600,level)
    tu.right(120)
    coch(600,level)
    tu.right(120)
    tu.hideturtle()
    tu.done()
main()
