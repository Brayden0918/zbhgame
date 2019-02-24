import turtle  #导入乌龟
t=turtle.Pen() #得到一支笔，赋值给变量t
t.forward(100) #前进100
t.left (90) #左转90度
t.forward (100) 
t.left (90) 
t.forward(100) 
t.left (90)
t.forward(100)
t.circle(50) #画一个半径50的圆
t.circle(50,180,6) #画一个180度、半径50、有六个面的线
t.circle(50,45,1) 
t.pencolor ("purple")
t.forward (100)
t.width (5)
t.forward (100)
t.penup()
t.left(90)
t.forward(100)
t.pendown()
t.forward(100)
t.speed(0)
t.width (5)
print (3==2)
print (3<2)

turtle.exitonclick()






