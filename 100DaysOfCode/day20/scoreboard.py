from turtle import Turtle

score = 0
ALIGNMENT = "center"
FONT = "Arial"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        with open("score.txt", "r") as f:
                self.high_score = int(f.read())
        self.speed("fastest")
        self.color("white")
        self.ht()
        self.score = 0
        self.write(f"Score : {self.score} High Score : {self.high_score}", align = ALIGNMENT, font = FONT)
    def increase(self):
        self.score += 1
        self.write(f"Score : {self.score}",False,align="center",font=("Arial",20,"normal"))
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over",False,align="center",font=("Arial",20,"normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align = ALIGNMENT, font = FONT)

        
