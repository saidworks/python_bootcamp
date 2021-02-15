from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.goto(0,0)
        self.pu()
        self.x_move = 5
        self.y_move = 5
        self.a = 0
        self.speed("slow")
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move 
        self.goto(new_x,new_y)  
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
    def _reset(self):
        self.goto(0,0)
        self.bounce_x()
    def increase_speed(self):
        if self.a <= 10:
            self.a += 1 
        self.speed(self.a)
        
  