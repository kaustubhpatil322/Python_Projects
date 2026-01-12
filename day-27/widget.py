from tkinter import *

#creating a new window and Configurations
window = Tk()
window.title("Widget  Examples")
window.minsize(width = 500 , height = 500)

#labels
label = Label(text = "This is old text")
label.config(text = "This is new Text")
label.pack()

#Buttons
def action():
    print("Do Something")

#Calls action() when Pressed
button = Button(text = "Click Me" , command = action)
button.pack() 

#Entries
entry = Entry(width = 30)
#add some text to Begin with
entry.insert(END , string = "Some text to begin with")

#Gets text in entry 
print(entry.get())
entry.pack()

#Text 
text = Text(height =5 , width =30)
#puts a cursor in textbox.
text.focus()
#Add some text to begin with.
text.insert(END , "Example of multi-line text entry.")
#Get current value in textbox at line 1 , character 0
print(text.get("1.0" , END))
text.pack()

#spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())

spinbox = Spinbox(from_ = 0 , to=10 , width = 5 , command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_ = 0 , to =100 , command = scale_used)
scale.pack()

#CheckButton
def checkbutton_used():
    #Prints 1 if on button Checked , Otherwise 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text = "Is On?", variable = checked_state , command= checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radio Button
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text = "Pikachu" , value = 100000 , variable = radio_state , command = radio_used)
radiobutton2= Radiobutton(text = "Bulbasour" , value = 200 , variable = radio_state , command = radio_used)
radiobutton3 = Radiobutton(text = "Snorlax" , value = 3000 , variable = radio_state , command = radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


#Listbox
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height = 5)
fruits = ["Apple" , "Pear" , "Orange" , "Banana" , "Lichi"]
for item in fruits:
    listbox.insert(fruits.index(item) ,  item)
listbox.bind("<<ListboxSelect>>" , listbox_used)
listbox.pack()
window.mainloop()
