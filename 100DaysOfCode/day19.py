from turtle import *

Said = Turtle()
screen = Screen()

def move_forward():
    Said.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()