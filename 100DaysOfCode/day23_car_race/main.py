import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# define instances of imported classes
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
# define actions
screen.onkey(player.move, 'Up')
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create()
    cars.move()
    for i in cars.all_cars:
        if player.distance(i)<20:
            print('you hit a car :( game over!')
            scoreboard.game_over()
            game_is_on = False

    if player.at_finish_line():
        player.at_start_line()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()