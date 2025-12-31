# Etch-A-Sketch
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkeypress(move_forward, "Up")
screen.onkey(move_backward, "s")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()