from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json    #json.load() , json.dump() , json.update() are its methods
#
FONT =("Courier" , 20 , "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    txt_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data_in_password_file(new_data):
    with open("password_data.json", "r") as password_file:
        # Load the Old data
        data  = json.load(password_file)
        # update the new data in the data variable
        data.update(new_data)
        # Now, open the json file in 'w' format to rewrite the updated data
        with open("password_data.json", "w") as password_file:
            json.dump(data, password_file, indent=4)
def save_data():
    email = txt_email.get()
    password = txt_password.get()
    website = txt_website.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }
    try:
        add_data_in_password_file(new_data)
    except Exception as err:
        #When Error is unknown , and you have to print the type of that exception USE THIS as below:
        print(f"Attention!!! There is an ERROR ={type(err).__name__}")
        with open("password_data.json" , "w") as password_file:
            json.dump({}, password_file)
        add_data_in_password_file(new_data)
    finally:
        txt_website.delete(first=0, last=END)
        txt_password.delete(first=0, last=END)
        txt_email.delete(first=0, last=END)
        txt_email.insert(0, "ksp29mar04@gmail.com")
        txt_website.focus()


def search_password():
    website = txt_website.get()
    ans = None
    try:
        with open("password_data.json" , "r") as password_file:
            data = json.load(password_file)
    except Exception as e:
        messagebox.showerror(title = "Error",
                             message=f"Error name = {type(e).__name__}")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(
            title= website,
            message = f"Email : {email}\nPassword : {password}",
        )
    else:
        messagebox.showerror(title="Error",
                            message="Website not Found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20 , pady=20)

canvas = Canvas(height = 200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image=logo_img)
canvas.grid(row=0 , column=1)

#labels
lbl_website = Label(text="Website:" , font=FONT  )
lbl_website.grid(row=1 , column= 0)

lbl_email = Label(text="Email/Username" , font = FONT )
lbl_email.grid(row=2, column =0)

lbl_password = Label(text="Password: " , font =FONT)
lbl_password.grid(row=3 , column = 0)

#Entries
txt_website = Entry(width=37 , justify="left")
txt_website.focus()
txt_website.grid(row=1 , column = 1 , columnspan=2)

txt_email = Entry(width=37 , justify = "left")
txt_email.insert( 0 , "ksp29mar04@gmail.com")#the 0 as parameter specifies the index at which the string to be Inserted
txt_email.grid(row =2 , column = 1 , columnspan = 2)

txt_password= Entry(width=21 , justify="left")
txt_password.grid(row=3, column=1)

#Buttons
btn_generate_password = Button(text = "Generate Password", width=12 , justify = "left" , command= generate_password)
btn_generate_password.grid(row=3, column=2)

btn_add = Button(text="Add" , width = 35 , command = save_data)
btn_add.grid(row = 4 , column = 1 , columnspan  =2)

btn_search = Button(text = "Search" , width =12 , justify="left" , command = search_password)
btn_search.grid(row=1 , column = 2)

window.mainloop()


