import random
from turtle import * 
import tkinter
said = Turtle()
said.pendown()
said.speed(10)
said.shape("arrow")
angle = 0
colormode(255)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


for i in range(360):
    said.circle(100)
    said.right(angle)
    angle += 1
    said.color(random_colors())

ts =said.getscreen()
ts.getcanvas().postscript(file="spirograph.eps")

