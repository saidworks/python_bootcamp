from turtle import *
from tkinter import *
import random
said = Turtle()
said.pd()
said.speed(10)
said.shape("turtle")
said.dot(4)
said.pensize(15)
# colors  = ["red","green","blue","orange","purple","pink","yellow","cyan","royal blue","orange red","gold","medium violet red","turquoise"]
colormode(255)
def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
angles = [0,90,180,270]
for i in range(1,1000,1):
    said.pencolor(random_colors())
    said.forward(30)
    said.seth(random.choice(angles))
    # if said.xcor()>500 or said.ycor > 500:
    #     said.backward(100)
        
ts =said.getscreen()
ts.getcanvas().postscript(file="randomwalk.eps")