from tkinter import *
FONT = ("Arial" , 14 , "bold")

def mile_to_km():
    mile_val = int(input_entry.get())
    km_val = mile_val  * 1.609
    label3.config(text =str(km_val))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 400 , height = 200)
window.config(padx =20 , pady =20)

input_entry = Entry(width =10)
input_entry.grid(row = 1 , column = 2)
input_entry.grid(padx = 20 , pady =20)

label1 = Label(text= "Miles" , font = FONT)
label1.grid(row = 1 , column = 3)
label1.config(padx=20 , pady = 10)

label2 = Label(text="is equal to" , font = FONT)
label2.grid(row = 2 , column = 1 )

label3 = Label(text = "0" , font = FONT)
label3.grid(row = 2 , column = 2)

label4 = Label(text = "Km" , font = FONT)
label4.grid(row = 2 , column = 3)

button = Button(text= "Calculate" ,command = mile_to_km)
button.grid(row= 3 , column= 2)
button.grid(pady = 20)



window.mainloop()




