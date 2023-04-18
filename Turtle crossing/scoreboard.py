from turtle import Turtle
ALIGNMENT="left"
FONT=('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.penup()
        self.goto(x=-230,y=220)
        self.write(f"level: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def new_score(self):
        self.score+=1
        self.clear()
        self.write(f"level: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
