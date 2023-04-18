from turtle import Screen,Turtle
from animal import Animal
from car import Cars
from scoreboard import Scoreboard
import time

screen =Screen()
screen.setup(width=500,height=500)
screen.bgcolor("white")
screen.title("Animal crossing ")
screen.tracer(0)

speed=0.1
turtle=Animal()
cars=Cars()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(turtle.go_up,"Up")


game_is_on=True
while game_is_on==True:
    screen.update()
    time.sleep(speed)

    cars.create_cars()
    cars.move_all()

    for car in cars.all_cars:
        if turtle.distance(car)<25:
            scoreboard.game_over()
            game_is_on = False

    if turtle.ycor()>230:
        turtle.go_home()
        speed*=0.8
        scoreboard.new_score()

screen.exitonclick()
