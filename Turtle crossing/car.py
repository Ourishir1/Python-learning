import random
from turtle import Turtle
from random import Random

COLORS=["red","orange","yellow","green","blue","purple"]


class Cars:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(y=random.randint(-200, 220), x=260)
            self.all_cars.append(new_car)

    def move_all(self):
        for car in self.all_cars:
            car.back(10)

