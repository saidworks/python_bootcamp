from turtle import *
from tkinter import *
import random
said = Turtle()
said.pd()
said.speed(10)
said.shape("turtle")
said.dot(4)
said.pensize(5)
colors  = ["red","green","blue","orange","purple","pink","yellow","cyan","royal blue","orange red","gold","medium violet red","turquoise"]
angles = [0,90,-90,180,360,-180,270]
for i in range(1,1000,1):
    said.color(random.choice(colors))
    said.forward(20)
    said.right(random.choice(angles))
    # if said.xcor()>500 or said.ycor > 500:
    #     said.backward(100)
        
ts =said.getscreen()
ts.getcanvas().postscript(file="randomwalk.eps")