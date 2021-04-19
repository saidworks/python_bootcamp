
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
#add check button
check_button = PhotoImage(file='icons8-check-box-with-check-48.png')
canvas.create_image(100,280,image=check_button)
canvas.pack()
#need to work using grid method 

window.mainloop()