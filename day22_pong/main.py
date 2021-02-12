from turtle import Screen,Turtle
from paddle import Paddle
import time
from ball import Ball
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
# creating the paddles and the ball
paddle_r = Paddle()
paddle_r.xcor = 350

paddle_l = Paddle()
paddle_l.goto(-350,0)
paddle_l.xcor=-350

ball = Ball()

#moving the paddles
screen.listen()
screen.onkey(paddle_r.up,"z")
screen.onkey(paddle_r.down,"s")
screen.onkey(paddle_l.up,"Up")
screen.onkey(paddle_l.down,"Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    #detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with paddle 
    if (ball.distance(paddle_r) < 50 and ball.xcor()>320) or (ball.distance(paddle_l) >-50 and ball.xcor()<-320):
        ball.bounce_x()
    
    
screen.exitonclick()