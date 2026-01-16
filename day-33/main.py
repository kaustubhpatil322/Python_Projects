
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# print(f"Latitude ={latitude} \nlongitude = {longitude}")


#---------------------------Kanye-Quote_Machine---------------------------------------------

import requests
from tkinter import *

#-------------------------Fetch-Quotes--------------------------------------------------------

response = requests.get(url="https://api.kanye.rest")
response.raise_for_status()#--> It checks the HTTP response status code and:
#
# ✅ Does nothing if the request was successful
# (status codes 200–299)
#
# ❌ Raises an exception if the request failed
# (status codes 400–599)


data = response.json()
print(data)
quote = data["quote"]


#----------------------------Interface------------------------------------------------------------

window = Tk()
window.title("Kanye_Quote_Machine")
window.config(padx=10 , pady=10)


quote_bg = PhotoImage(file="Yellow_canvas.png")
canvas = Canvas(width=500, height=500)
canvas.create_image(250 , 200 ,image=quote_bg)
canvas.create_text(250 , 150 ,width=200, text=quote , font=("Ariel" , 20 , "italic"))
canvas.grid(row=0, column=0)

canvas2 = Canvas(width = 400 , height = 50 )
kanye = PhotoImage(file="kanye.png")
canvas.create_image(150 , 400 , image=kanye)
canvas2.grid(row=1 , column=0)

window.mainloop()
