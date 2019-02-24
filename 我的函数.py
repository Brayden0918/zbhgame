import turtle
t=turtle.Pen()

#画n个圆
def draw(n):
    t.home()
    t.clear()
    for x in range(n):
        t.circle(x*10)

#打印数字区间能被n整除的数
def mode(start,end,n):
    for x in range(start,end):
        if x%n == 0:
            print(x)
