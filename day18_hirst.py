import random
from turtle import * 
import tkinter
said = Turtle()
mau = Screen()
mau.screensize(600,600)
said.pu()
said.speed(10)
# said.setx(-300)
said.sety(380)
colormode(255)
def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
for j in range(13):
    said.setx(-600)
    said.pu()
    for i in range(20):
        said.pendown()
        said.pencolor(random_colors())
        said.dot(30)
        said.pu()
        said.forward(60)
    said.right(90)
    said.forward(60)
    said.right(-90)

ts =said.getscreen()
ts.getcanvas().postscript(file="histpaint.eps")
