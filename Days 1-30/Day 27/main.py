from tkinter import *

def miles_to_km():
    miles = int(entrybox.get())
    text4.config(text = "%.0f" % (miles * 1.6))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 400 , height = 150)

text1 = Label(text="is equal to")
text1.grid(column = 0 , row = 1)

text2 = Label(text = "Miles") 
text2.grid(column = 2 , row = 0)

text3 = Label(text = "Kilometer")
text3.grid(column = 2 , row = 1)

text4 = Label(text = 0)
text4.grid(column = 1 , row = 1)

button = Button(text = "Calculate" , command = miles_to_km)
button.grid(column = 1 , row = 2)

entrybox = Entry(width = 10)
entrybox.grid(column = 1 , row = 0)



window.mainloop()