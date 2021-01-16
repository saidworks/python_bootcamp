from turtle import Screen,Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")

paddle_1 = Paddle()
screen.listen()
screen.onkey(paddle_1.up,"Up")
screen.onkey(paddle_1.down,"Down")


screen.exitonclick()