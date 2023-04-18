import turtle
from turtle import Screen
import pandas


screen=Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
points=0
guessed_states=[]

while points < 51:
    Guess=screen.textinput(title=f"{points}/50 States Correct",prompt="Name a state").title()
    if Guess == "Exit":
        missing_states =[state for state in all_states if state not in guessed_states]
        new_data =pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if Guess in all_states:
        guessed_states.append(Guess)
        t = turtle.Turtle()
        t.hideturtle()
        state_data = data[data.state == Guess]
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(Guess)
        points+=1


screen.exitonclick()