# The famous Snake Game
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

BORDER_PAD = 280
SNAKE_FOOD_DISTANCE = 15

is_game_started = False
screen = Screen()
screen.setup(width=600, height=600)
game_start = screen.textinput(title="Start the Game", prompt="Let's start the game? 'Y' or 'N': ")
screen.bgcolor("black")
screen.title("Snake's Zoo")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

if game_start.lower() == "y":
    is_game_started = True
    
while is_game_started:
    screen.update()
    time.sleep(0.1)
    scoreboard
    snake.move()
    
    #Collision with food
    if snake.head.distance(food) < SNAKE_FOOD_DISTANCE:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
        
    #Detect collision with wall
    if snake.head.xcor() > BORDER_PAD or snake.head.xcor() < -BORDER_PAD or snake.head.ycor() > BORDER_PAD or snake.head.ycor() < -BORDER_PAD:
        scoreboard.game_over()
        is_game_started = False
        
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_started = False
screen.exitonclick()