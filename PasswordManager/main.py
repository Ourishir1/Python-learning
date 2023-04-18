from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_pass():
    password.delete(0,END)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list= password_letters + password_symbols + password_numbers

    shuffle(password_list)

    random_pass="".join(password_list)
    password.insert(END,F"{random_pass}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_entery=website.get()
    email_entery=user_email.get()
    password_entery=password.get()
    new_data = {website_entery:{
        "email":email_entery,
        "password":password_entery
        }
    }
    if len(email_entery) == 0 or len(website_entery) == 0 or password_entery == 0:
        messagebox.showerror(title="Ooops",message="Hey! don't leave any fields empty!")

    else:
        try:
            with open("data.json","r") as data_file:
                data =json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data, data_file,indent=4)

        finally:
            website.delete(0,END)
            password.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_password():
    web=website.get()
    with open("data.json","r") as data_file:
        user_data=json.load(data_file)
        site=user_data.get(web)
        try:
            password=site.get('password')
        except AttributeError:
            messagebox.showerror(title="Ooops", message=f"There is no {web} on the list. try again")
        else:
            email= site.get('email')
            messagebox.showinfo(title=f"{web}",message=f"the email is {email}\n"
                                                              f"the password is {password}")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
pass_img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image= pass_img)
canvas.grid(row=0,column=1)


web_label=Label(text="Website:")
web_label.grid(row=1, column=0)
website=Entry(width=34)
website.grid(row=1, column=1,columnspan=1)
website.focus()

user_label=Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_email=Entry(width=52)
user_email.grid(row=2, column=1, columnspan=2)
user_email.insert(END, "ourishir1@gmail.com")

pass_label=Label(text="Password:")
pass_label.grid(row=3, column=0)
password=Entry(width=34)
password.grid(row=3,column=1)

Generate_pass=Button(text="Generate Password",command=get_pass)
Generate_pass.grid(row=3,column=2)
add_button=Button(text="Add",width=44,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

search_but=Button(text="Search",command=search_password,width=15)
search_but.grid(row=1,column=2)

window.mainloop()