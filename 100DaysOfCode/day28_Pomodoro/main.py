
from tkinter import *
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

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro technique")
window.config(padx=100,pady=50,bg=YELLOW)
#create canvas for tomato image
canvas = Canvas(width=200,height=300,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,120,image=tomato_img)
canvas.create_text(100,150,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
#add check and buttons
check = Canvas(48,48,bg=YELLOW,highlightthickness=0)
check_button = PhotoImage(file='icons8-check-box-with-check-48.png')
check.create_image(width=100,height=280,image=check_button)
check.grid(row=2,column=1)
start = Button(text='start')
start.grid(row=2,column=0)

#need to work using grid method 
canvas.grid(row=1,column=1)
window.mainloop()