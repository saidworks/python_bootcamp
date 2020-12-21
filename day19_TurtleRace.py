from turtle import Turtle, Screen
import random


# common main setup
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet",prompt="which turtle will win the race: ")
colors = ["red","green","blue","orange","purple","pink","yellow"]
def shape_color(turtle):
    # turtle.color(random.choice(colors))
    turtle.shape("turtle")
    turtle.pu()

# Turtle definition
red = Turtle()
green = Turtle()
blue = Turtle()
orange = Turtle()
purple = Turtle()
Turtles = [red,green,blue,orange,purple] 
# turtle colors and shape
i = 0 
for turtle in Turtles:
    shape_color(turtle)
    turtle.color(colors[i])
    i +=1


# Turtle start position
red.goto(x=-200,y=-150)
green.goto(x=-200,y=100)
blue.goto(x=-200,y=-100)
orange.goto(x=-200,y=0)
purple.goto(x=-200,y=50)


# turtle moving 
for i in range(15):
    for turtle in Turtles:
        if turtle.xcor() <= 210:
            turtle.forward(random.randint(10,50))
fastest = 0
for a in Turtles:
    for b in Turtles:
        if a.xcor() > b.xcor() and a.xcor() > fastest : 
                fastest = a.xcor()
for turtle in Turtles:
    if turtle.xcor() == fastest:
        print(f"The winner is {turtle.fillcolor()}")
        if bet == turtle.fillcolor():
            print("You won! congratulations!")
        else: 
            print("you lost :( try again!")            
        

screen.exitonclick()


