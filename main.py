from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()
screen.listen()

def fw():
    tim.forward(10)

def bw():
    tim.back(10)

def ccw():
    tim.left(10)

def cw():
    tim.right(10)

def cl():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key="w", fun=fw)
screen.onkey(key="s", fun=bw)
screen.onkey(key="a", fun=ccw)
screen.onkey(key="d", fun=cw)
screen.onkey(key="c", fun=cl)



screen.exitonclick()