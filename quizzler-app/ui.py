from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
FONT_NAME="Ariel"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.score=Label(text=f"Score: 0",font=(FONT_NAME, 12, "italic"),bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question_text=self.canvas.create_text(150,125,
                                width=280,
                                text="enter text here",
                                fill=THEME_COLOR,
                                font=(FONT_NAME, 20, "italic")
                                )

        CHECK_IMG = PhotoImage(file="./images/true.png")
        self.check=Button(image=CHECK_IMG, highlightthickness=0, command=self.true_pressed)
        self.check.grid(row=2,column=0)

        X_IMG = PhotoImage(file="./images/false.png")
        self.x=Button(image=X_IMG,highlightthickness=0,command=self.false_pressed)
        self.x.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="THE END")
            self.check.config(state="disabled")
            self.x.config(state="disabled")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self,check):
        if check == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)