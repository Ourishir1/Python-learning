from turtle import Turtle

MOVE_DISTANCE = 10

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(y=-230, x=0)
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_home(self):
        self.goto(y=-230, x=0)
