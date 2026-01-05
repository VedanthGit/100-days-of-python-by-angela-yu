import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
SCOREBOARD_LOC = (0, 270)

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "data.txt")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as data:
                data.write("0")

        with open(DATA_FILE) as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(SCOREBOARD_LOC)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()