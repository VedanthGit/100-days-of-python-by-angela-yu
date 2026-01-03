# The Pong Game
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WINNING_SCORE = 1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

user_1_paddle = Paddle((-380, 0))
user_2_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(user_1_paddle.go_up, "w")
screen.onkeypress(user_1_paddle.go_down, "s")
screen.onkeypress(user_2_paddle.go_up, "Up")
screen.onkeypress(user_2_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if scoreboard.user_1_score == WINNING_SCORE or scoreboard.user_2_score == WINNING_SCORE:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with wall on top and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Bounce
        ball.bounce()
        
    # Detect collision with paddle
    if (ball.distance(user_2_paddle) < 70 and ball.xcor() > 350)or (ball.distance(user_1_paddle) < 70 and ball.xcor() < -350):
        ball.reflect()
    
    # Detect the ball if it misses the paddle
    if ball.xcor() > 390:
        ball.reset_position()
        user_1_paddle.reset_position()
        user_2_paddle.reset_position()
        scoreboard.user_1_point()
        
    if ball.xcor() < -390:
        ball.reset_position()
        user_1_paddle.reset_position()
        user_2_paddle.reset_position()
        scoreboard.user_2_point()
    

screen.exitonclick()