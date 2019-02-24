#我的随机泡泡
import turtle
from random import *

turtle.colormode(255)
t=turtle.Pen()
t.speed(0)
for i in range(100):
    r1=randint(0,255)
    g1=randint(0,255)
    b1=randint(0,255)

    r2=randint(0,255)
    g2=randint(0,255)
    b2=randint(0,255)         
    
    x=randint(-400,400)
    y=randint(-400,400)
    rad=randint(50,200)
    width=randint(1,10)
    
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.width(width)
    t.fillcolor(r1,g1,b1)
    t.pencolor(r2,g2,b2)
    t.begin_fill()
    t.circle(rad,randint(0,360),randint(3,50))
    t.end_fill()
    
    
