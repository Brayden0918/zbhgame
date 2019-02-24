import turtle
t = turtle.Pen()

turtle.bgcolor("black")
sides = 6
t.speed(0)
colors = ["red","yellow","blue","orange","green","purple"]

for x in range(80):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)

t.penup()
t.home()
t.right(90)
t.pendown ()
t.width(3)
t.pencolor("purple")
t.penup()
t.fd(75)
t.pendown()
t.fd(250)
