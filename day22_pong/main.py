from turtle import Screen,Turtle
from paddle import *
import time
from ball import Ball
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
# creating the paddles and the ball
paddle_1 = Paddle()
paddle_1.xcor = 350

paddle_2 = Paddle()
paddle_2.goto(-350,0)
paddle_2.xcor=-350

ball = Ball()

#moving the paddles
screen.listen()
screen.onkey(paddle_1.up,"z")
screen.onkey(paddle_1.down,"s")
screen.onkey(paddle_2.up,"Up")
screen.onkey(paddle_2.down,"Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()