from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.write(f"{self.score_1} : {self.score_2} ",align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def new_score_1(self):
        self.score_1 +=1
        self.clear()
        self.write(f"{self.score_1} : {self.score_2} ",align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def new_score_2(self):
        self.score_2 += 1
        self.clear()
        self.write(f"{self.score_1} : {self.score_2} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()