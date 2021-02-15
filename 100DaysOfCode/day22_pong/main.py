from turtle import Screen,Turtle
from paddle import Paddle
import time
import math
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
# creating the paddles ,the ball and the scoreboard
paddle_r = Paddle()
paddle_r.xcor = 350

paddle_l = Paddle()
paddle_l.goto(-350,0)
paddle_l.xcor=-350

ball = Ball()

scoreboard = Scoreboard()

#moving the paddles
screen.listen()
screen.onkey(paddle_r.up,"z")
screen.onkey(paddle_r.down,"s")
screen.onkey(paddle_l.up,"Up")
screen.onkey(paddle_l.down,"Down")

""" Incease level difficulty by changing the speed of the ball: 
the idea: divide time laps by 2 each time the ball hits the paddle"""
difficulty = 0.05

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(difficulty)
    ball.move()
    #detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with paddle 
    if (ball.distance(paddle_r) < 50 and ball.xcor()>350) or (ball.distance(paddle_l)< 50 and ball.xcor()<-350):
        ball.bounce_x()
        ball.increase_speed()
        difficulty /= 2
    #detect when the ball goes offscreen
    if ball.xcor()>380: 
        ball._reset()
        scoreboard.l_point()
    elif ball.xcor()<-380:
        ball._reset()
        scoreboard.r_point()
    #end game
    if scoreboard.l_score >= 50:
        print("the player in the left won the game congratulations!")
        game_is_on = False

        
screen.exitonclick()