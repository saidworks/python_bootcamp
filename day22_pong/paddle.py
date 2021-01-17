from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square") 
        self.color ("white")
        self.shapesize(5,1)
        self.goto(350,0)
        self.pos()
        self.y = 0
        self.speed("fastest")
    def up(self):
        self.y += 10
        self.setheading(0)
        self.goto(self.xcor,self.y)
            
        
    def down(self):
        self.y -= 10
        self.setheading(0)
        self.goto(self.xcor,self.y)

