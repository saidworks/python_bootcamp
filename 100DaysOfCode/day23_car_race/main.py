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
car = CarManager()
# define actions
screen.onkey(player.move, 'Up')
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    for i in car.all_cars:
        if player.distance(i)<50:
            print('you hit a car :( game over!')
            game_is_on = False

    if player.at_finish_line():
        player.at_start_line()
        player.clear()

screen.exitonclick()