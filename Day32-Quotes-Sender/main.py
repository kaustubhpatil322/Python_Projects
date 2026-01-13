import smtplib
import random
import datetime as dt


now = dt.datetime.now()
quotes_arr=[]
with open("quotes.txt" , "r") as file:
    quotes_arr = file.readlines()
#
my_msg = random.choice(quotes_arr)
# my_email = "ksp29mar04@gmail.com"
# my_password = "vgjb iwlr xzvv emfq"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email , password= my_password)
#     connection.sendmail(from_addr= my_email ,
#                         to_addrs = "patilks322@gmail.com ",
#                         msg="Subject:Headspace Quotes\n\n"+my_msg)

EMAIL = "ksp29mar04@gmail.com"
MY_PASS = "vgjb iwlr xzvv emfq"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(EMAIL , MY_PASS)
    connection.sendmail(from_addr=EMAIL , to_addrs = "patilks322@gmail.com" ,
                        msg="Subject:Quotes to start your Day\n\n"+my_msg)
