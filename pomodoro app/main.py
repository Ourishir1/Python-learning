from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer")
    mark.config(text="")
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec= LONG_BREAK_MIN * 60
    if reps % 2 == 0 :
        count_down(short_break_sec)
        text.config(text="Take a short break",fg=PINK)
        reps+=1
    elif reps % 8 == 0:
        count_down(long_break_sec)
        text.config(text="GYM TIME !",fg=RED)
        reps+=1
    else:
        count_down(work_sec)
        text.config(text="WORK WORK WORK")
        reps+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_sec = count % 60
    minutes=math.floor(count/60)
    if count_sec == 0 or count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{int(minutes)}:{count_sec}")
    global timer
    if count > 0:
        timer = canvas.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
screen=Tk()
screen.title("Pomodoro")
screen.config(padx=100,pady=50, bg=YELLOW)

canvas=Canvas(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(190,112, image=tomato_img)
timer_text=canvas.create_text(190,130,text="00:00",fill="white",font=(FONT_NAME, 30, "bold"),justify="center")
canvas.grid(row=1,column=1)


text=Label(text="Timer",fg=GREEN,font=(FONT_NAME, 50),bg=YELLOW)
text.grid(row=0,column=1)

start_bt=Button(text="Start",highlightthickness=0,command=start_timer)
start_bt.grid(row=2,column=0,)

reset_bt=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_bt.grid(row=2,column=2)

mark=Label(text="",fg=GREEN,font=(FONT_NAME, 10) ,bg=YELLOW)
mark.grid(row=3,column=1)

screen.mainloop()