import  pandas
import datetime as dt
import smtplib
from random import randint

time = dt.datetime.now()
my_email = "ourishircourse@gmail.com"
my_password = "nhnnnzbpeknfymxc"


data=pandas.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient="records")


for friend in birthday_list:
    if friend["month"] == time.month and friend["day"] == time.day:
        file_path=f"letter_temp/letter_{randint(1,3)}.txt"
        with open(file_path) as letter_file:
            content=letter_file.read()
            new_content=content.replace("[NAME]",friend["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs="ourishir1@yahoo.com",
                                msg=f"Subject:Happy birthday {friend['name']}\n\n"
                                    f"{new_content}")





# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




