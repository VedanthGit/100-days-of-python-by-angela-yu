from turtle import Turtle
FONT = ("Courier", 16, "normal")
SCORE_LOC = (-280, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        
    def score_point(self):
        self.score += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_LOC)
        self.write(f"Level: {self.score}", align="left", font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        
        self.write(f"Your score is: {self.score-1}", align="center", font=FONT)