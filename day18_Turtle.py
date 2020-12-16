from turtle import Turtle,Screen
import random

maureen = Turtle()
maureen.shape("turtle")
maureen.color("dodger blue")
said = Screen()
maureen.speed(4)
maureen.pencolor("dodger blue")
maureen.pendown()

#draw a square
for i in range(4):
    maureen.forward(100)
    maureen.right(90)

maureen.penup()
maureen.goto(-200,50)
maureen.pd()

# draw a dashed line
for i in range(25):
    maureen.forward(10)
    maureen.penup()
    maureen.forward(10)
    maureen.pendown()

#draw different shapes
maureen.pu()
maureen.goto(0,0)
maureen.pd()
colors = ["royal blue","dark green","lime","dark orange","magenta","saddle brown"]

maureen.forward(100)
maureen.right(60)
maureen.forward(50)
maureen.left(120)
maureen.goto(0,0)
for i in range(4):
     maureen.forward(100)
     maureen.right(90)

