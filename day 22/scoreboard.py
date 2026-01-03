from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
USER_1_SCOREBOARD_LOC = (-50, 260)
USER_2_SCOREBOARD_LOC = (50, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_1_score = 0
        self.user_2_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def user_1_point(self):
        self.user_1_score += 1
        self.update_scoreboard()
        
    def user_2_point(self):
        self.user_2_score += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(USER_1_SCOREBOARD_LOC)
        self.write(self.user_1_score, align=ALIGNMENT, font=FONT)
        self.goto(USER_2_SCOREBOARD_LOC)
        self.write(self.user_2_score, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0, 15)
        self.write("THE PONG GAME", align="center", font=("Courier", 36, "bold"))
        self.goto(0, -60)

        if self.user_1_score > self.user_2_score:
            winner_text = "PLAYER 1 WINS"
        elif self.user_2_score > self.user_1_score:
            winner_text = "PLAYER 2 WINS"
        else:
            winner_text = "DRAW"

        self.write(winner_text, align="center", font=("Courier", 36, "bold"))

