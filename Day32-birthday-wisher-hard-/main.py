##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas
import datetime as dt
import smtplib

data = pandas.read_csv("birthdays.csv")

data_dict = data.to_dict(orient="records")
print(data_dict)

now = dt.datetime.now()
day = now.day
month = now.month

MY_EMAIL = "ksp29mar04@gmail.com"
MY_PASS = "ttld hlex xrka xrbb" #Generated APP PASSWORD

person=None
for entry in data_dict:
    if entry["month"] == month and entry["day"] == day:
        person = entry

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL , MY_PASS)
    connection.sendmail(from_addr=MY_EMAIL , to_addrs=person["email"] ,
                         msg="Subject:Wishes on your Birthday\n\nHAPPy BIRThDAy To YOu, the most cheerfull person in the world.")








