import turtle
t=turtle.Pen()
turtle.colormode(255)
t.speed(0)
for x in range(255):
    t.width(1)
    r=x%255
    g=x%255
    b=x%255
    t.pencolor(r,200,100)
    t.fd(x)
    t.left(10)
    t.pencolor(100,g,200)
    t.fd(x)
    t.left(10)
    t.pencolor(200,100,b)
    t.fd(x)
    t.left(10)
    
    
