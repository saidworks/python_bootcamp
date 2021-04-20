
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(t):
    while t:
        seconds = t * 60
        time.sleep(1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro technique")
window.config(padx=100,pady=50,bg=YELLOW)
#create canvas for tomato image
canvas = Canvas(width=200,height=300,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,120,image=tomato_img)
canvas.create_text(100,150,text='00:00',fill="white",font=(FONT_NAME,35,"bold"))
#add title, check and buttons
title = Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW,highlightthickness=0)
title.grid(row=0,column=1)
check = Canvas(width=40,height=40,bg=YELLOW)
check_button = PhotoImage(file='icons8-check-box-with-check-48.png')
check.create_image(20,20,image=check_button)
check.grid(row=3,column=1)
start = Button(text='start',padx=10)
start.grid(row=2,column=0)
reset = Button(text='reset',padx=10)
reset.grid(row=2,column=3)

#need to work using grid method 
canvas.grid(row=1,column=1)
window.mainloop()