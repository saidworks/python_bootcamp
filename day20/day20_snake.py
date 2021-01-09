from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setup screen 
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
#move on events (specified keys pressed)
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.listen()
game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()   
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    # detect collision with wall 
    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()
    # detect collision with tail
        # if head collides with any segments of the snake 
            #trigger game over sequence
    for segment in snake.segments:
        if segment != snake.head:
            if segment.distance(snake.head) < 10:
                game_is_on = False
                scoreboard.game_over()


screen.exitonclick()