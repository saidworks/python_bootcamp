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

    def move(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.y_position += MOVE_DISTANCE
        self.goto(0,self.y_position,)

