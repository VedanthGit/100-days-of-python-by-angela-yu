import turtle
import time
import random

screen = turtle.Screen()
screen.title("BREAKOUT")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

score = 0

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.color("white")
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 7.5
ball.dy = 7.5


bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

start_x = -350
start_y = 200

for row in range(4):
    for col in range(10):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(start_x + col * 75, start_y - row * 40)
        bricks.append(brick)


def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 80)


def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 80)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

game_over = False


while True:
    screen.update()
    time.sleep(0.01)

    if game_over:
        score_pen.goto(-350, 200)
        score_pen.clear()
        score_pen.write(
            f"GAME OVER\nFinal Score: {score}",
            align="center",
            font=("Arial", 20, "bold"),
        )
        break

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        print(f"score: {score}")
        game_over = True

    if (
        -260 < ball.ycor() < -240
        and paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60
    ):
        ball.sety(-240)
        ball.dy *= -1

    for brick in bricks[:]:
        if ball.distance(brick) < 35:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            score_pen.clear()
            score_pen.write(
                f"Score: {score}", align="center", font=("Arial", 16, "normal")
            )
