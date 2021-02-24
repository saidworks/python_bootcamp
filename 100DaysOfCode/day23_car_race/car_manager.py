from turtle import Turtle, xcor, ycor
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self): 
        self.all_cars = []
    def create(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move(self):
        random_y= random.randint(5,10)
        for car in self.all_cars:
            car.backward(car.ycor()+random_y)