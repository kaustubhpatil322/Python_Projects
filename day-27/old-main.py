from tkinter import *

def button_clicked():
    print("I got Clicked")
    # if my_label["text"] == "I got Clicked":
    #     my_label.config(text = "I got Kicked")
    # else:
    #     my_label.config(text = "I got Clicked")
    my_label.config(text = input_entry.get())
    print(input_entry.get())


window = Tk()
window.title("my first gui program")
window.minsize(width=500 , height = 300)
window.config(padx = 200 , pady = 200)

#There 3 Layout Managers = pack , grid , place

my_label = Label(text = "I am Label" , font=("Arial" , 24 , "bold"))
my_label["text"] = "I am Kaustubh"
my_label.config(text="I am Kaustubh")
my_label.grid(row = 1 , column = 1)
my_label.config(padx = 50 , pady = 50)
# my_label.place(x = 200 , y = 200)
# my_label.pack() #my_label will not show up unless you write this

button = Button(text = "Click Me", command = button_clicked)
button.grid(row = 2  , column = 2)
# button.pack()

input_entry = Entry(width = 10)
print(input_entry.get())
input_entry.grid(row = 3 , column = 4)
# input_entry.pack() #This line is always needed to show the above content on the window

new_n=button = Button(text = "Click new")
button.grid(row = 1 , column = 3)




window.mainloop()


#passing unlimited positional  arguments to the Function
def add(*chi):#the IMPORTANT part is putting * before chi/args
    ans=0
    print(type(chi))
    for arg in chi:
        ans += arg
    print(ans)
add(1,2,3)
add(44,55,66,7 , -3 , -4 , -100)

#Passing unlimited Keyword arguments
def calculate(**kwargs):#The most IMPORTANT part  is  putting ** before kwargs
    print(kwargs) #Here, kwargs is the Dictionary (Very Important)
    str_all= ""
    for term in kwargs:
        str_all += kwargs[term]
    print(str_all)
calculate(add = "+" ,mul = "*" , sub = "-" , div = "/")