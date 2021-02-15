from turtle import Turtle

score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.speed("fastest")
        self.color("white")
        self.ht()
        self.score = 0
        self.write(f"Score : {self.score}",False,align="center",font=("Arial",20,"normal"))
    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}",False,align="center",font=("Arial",20,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",False,align="center",font=("Arial",20,"normal"))

        
