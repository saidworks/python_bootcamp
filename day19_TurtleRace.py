from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
screen.textinput(title="Make your bet",prompt="which turtle will win the race: ")
colors = ["red","green","blue","orange","purple","pink","yellow","cyan","royal blue","orange red","gold","medium violet red","turquoise"]

tim = Turtle()

tim.goto(-200,-150)
screen.exitonclick()