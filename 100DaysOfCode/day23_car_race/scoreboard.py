from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-100,250)
        self.write(f'level : {self.level}',align='left',font=FONT)
    
    def update_level(self):
        self.clear()
        self.write(f'level : {self.level}',align='left',font=FONT)

    def increase_level(self):
        self.level += 1 
        self.update_level()

    def game_over(self):
        self.goto(-50,0)
        self.write('Game over!',align='center',font=FONT)


    

