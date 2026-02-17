import time
import turtle
import random


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("SPACE INVADERS")
screen.tracer(0)

score = 0
score_pen = turtle.Turtle(visible=False)
score_pen.penup()
score_pen.color("white")
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.shapesize(stretch_wid=1.2, stretch_len=1.2)
player.penup()
player.setheading(90)
player.goto(0, -250)
player.speed(0)

PLAYER_SPEED = 20

bullet = turtle.Turtle()
bullet.shape("square")
bullet.shapesize(stretch_wid=0.3, stretch_len=0.3)
bullet.penup()
bullet.hideturtle()
bullet.speed(0)
bullet.dy = 20
bullet_state = "ready"

aliens = []
ALIEN_ROWS = 3
ALIEN_COLS = 7
ALIEN_START_Y = 200
ALIEN_SPACING_X = 80
ALIEN_SPACING_Y = 50
ALIEN_SPEED_X = 5
ALIEN_DESCEND = 20
alien_dx = ALIEN_SPEED_X

for row in range(ALIEN_ROWS):
    for col in range(ALIEN_COLS):
        alien = turtle.Turtle()
        alien.shape("circle")
        alien.color("lime")
        alien.penup()
        alien.goto(-240 + col * ALIEN_SPACING_X, ALIEN_START_Y - row * ALIEN_SPACING_Y)
        aliens.append(alien)

barriers = []
BARRIER_Y = -150
for x in [-200, 0, 200]:
    for i in range(3):
        block = turtle.Turtle()
        block.shape("square")
        block.color("cyan")
        block.shapesize(stretch_wid=0.6, stretch_len=1.2)
        block.penup()
        block.goto(x + i * 20 - 20, BARRIER_Y)
        barriers.append(block)


def move_left():
    x = player.xcor()
    if x > -360:
        player.setx(x - PLAYER_SPEED)


def move_right():
    x = player.xcor()
    if x < 360:
        player.setx(x + PLAYER_SPEED)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fired"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")


def is_collision(a, b, threshold=20):
    return a.distance(b) < threshold


game_over = False
last_descend = time.time()

while True:
    screen.update()
    time.sleep(0.02)

    if game_over:
        score_pen.goto(0, 0)
        score_pen.clear()
        score_pen.write(
            f"GAME OVER\nFinal Score: {score}",
            align="center",
            font=("Arial", 20, "bold"),
        )
        break

    edge_hit = False
    for alien in aliens:
        x = alien.xcor() + alien_dx
        alien.setx(x)
        if x > 370 or x < -370:
            edge_hit = True

    if edge_hit and time.time() - last_descend > 0.5:
        alien_dx *= -1
        for alien in aliens:
            alien.sety(alien.ycor() - ALIEN_DESCEND)
        last_descend = time.time()

    for alien in aliens:
        if alien.ycor() < -220:
            game_over = True

    for alien in aliens[:]:
        if bullet_state == "fired" and is_collision(bullet, alien, 20):
            bullet.hideturtle()
            bullet_state = "ready"
            alien.goto(1000, 1000)
            alien.remove(alien)
            score += 10
            score_pen.clear()
            score_pen.write(
                f"Score: {score}", align="center", font=("Arial", 16, "normal")
            )

    if not aliens:
        score_pen.goto(0, 0)
        score_pen.clear()
        score_pen.write(
            f"YOU WIN!\nFinal Score: {score}",
            align="center",
            font=("Arial", 20, "bold"),
        )
        break

turtle.done()
