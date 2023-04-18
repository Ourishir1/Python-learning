from turtle import Screen,Turtle
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen =Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

speed=0.1
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_is_on=True

while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed *= 0.5

    if ball.xcor() > 380:
        scoreboard.new_score_1()
        ball.home()
        ball.bounce_x()
        speed=0.1

    if ball.xcor() < -380:
        scoreboard.new_score_2()
        ball.home()
        ball.bounce_x()
        speed=0.1

screen.exitonclick()
