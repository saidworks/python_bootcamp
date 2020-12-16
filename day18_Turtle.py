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

# draw a triangle 
maureen.color(random.choice(colors))
maureen.forward(100)
maureen.right(120)
maureen.forward(100)
maureen.right(120)
maureen.forward(100)

#draw a square
maureen.home()
maureen.color(random.choice(colors))
for i in range(4):
      maureen.forward(100)
      maureen.right(90)

# draw a pentagon 
maureen.home()
maureen.color(random.choice(colors))
for i in range(5):
    maureen.forward(100)
    maureen.right(72)

# draw a hexagon
maureen.home()
maureen.color(random.choice(colors))
for i in range(6):
    maureen.forward(100)
    maureen.right(60)

# draw a heptagon
maureen.home()
maureen.color(random.choice(colors))
for i in range(7):
    maureen.forward(100)
    maureen.right(360/7)

# draw an octagon
maureen.home()
maureen.color(random.choice(colors))
for i in range(8):
    maureen.forward(100)
    maureen.right(360/8)

# draw an nonagon
maureen.home()
maureen.color(random.choice(colors))
for i in range(9):
    maureen.forward(100)
    maureen.right(360/9)

# draw an decagon
maureen.home()
maureen.color(random.choice(colors))
for i in range(10):
    maureen.forward(100)
    maureen.right(360/10)

