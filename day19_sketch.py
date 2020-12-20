from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(30)

def turn_anticlockwise():
    tim.left(30)

def clear_screen():
    screen.clearscreen()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=turn_anticlockwise)
screen.onkey(key="D", fun=turn_clockwise)
screen.onkey(key="C", fun=clear_screen)
screen.exitonclick()
