from car_manager import MOVE_INCREMENT
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape("turtle")
        self.setheading(90)
        self.pu()
        self.goto(STARTING_POSITION)
        self.y_position = -280
    def at_start_line(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
   

