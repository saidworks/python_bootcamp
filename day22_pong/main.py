from turtle import Screen,Turtle
from paddle import *
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0,1)
# creating the paddles
paddle_1 = Paddle()


#moving the paddles
game_is_on = True

while game_is_on: 
    screen.listen()
    screen.update()

    screen.onkey(paddle_1.up,"Up")
    screen.onkey(paddle_1.down,"Down")


screen.exitonclick()