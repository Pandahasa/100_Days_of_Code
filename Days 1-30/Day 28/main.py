
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    text1.config(text = "Timer" , fg = GREEN)
    global reps
    reps = 0
    canvas.itemconfig(timer_text , text = "00:00")
    window.after_cancel(timer)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def begin_timer():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    lbreak_sec = LONG_BREAK_MIN * 60
    checkmark.config(text = math.floor(reps / 2)* "✔")
    if reps % 8 == 0:
        text1.config(text = "Break" , fg = RED)
        countdown(lbreak_sec)
    elif reps % 2 == 1:
        text1.config(text = "Work" , fg = GREEN)
        countdown(work_sec)
    else:
        text1.config(text = "Break" , fg = PINK)
        countdown(break_sec)
  


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text , text = f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000 , countdown , count - 1)
    else:
        begin_timer()

            
            
        
        
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady = 50 , bg = YELLOW)


canvas  = Canvas(width = 200 , height = 224 , bg = YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100 , 112 , image = tomato_img)
timer_text = canvas.create_text(103 , 130 , text = "00:00" , fill ="white" , font = (FONT_NAME , 35 , "bold"))
canvas.grid(column = 1 , row = 1)

text1 = Label(text = "Timer" , font = (FONT_NAME , 45 , "bold") , fg = GREEN , bg = YELLOW)
text1.grid(column = 1 , row = 0)

checkmark = Label(text = "")
checkmark.grid(column = 1 , row = 3)

start_button = Button(text = "Start" , command = begin_timer)
start_button.grid(column = 0 , row = 2)

reset_button = Button(text = "Reset" , command = timer_reset)
reset_button.grid(column = 2 , row = 2)


window.mainloop()