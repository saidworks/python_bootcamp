from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.goto(0,0)
        self.pu()
    def move(self):
        self.goto(self.xcor()+10,self.ycor()+10)    