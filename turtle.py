import turtle
from turtle import *

wn = turtle.Screen()
wn.title("Turtle 1.O")
wn.setup(width=800, height=600)
turtle.bgcolor("black")
turtle.pencolor("blue")
turtle.hideturtle()

#objected, position

penup()
goto(-2, 0)
pendown()

for i in range(1, 1092):
    turtle.speed(0)
    circle(1, 2, 3)
    circle(1 + i, 2 + i, 3 + i)
    i = i + 1
    turtle.hideturtle()


turtle.update()
turtle.done()
