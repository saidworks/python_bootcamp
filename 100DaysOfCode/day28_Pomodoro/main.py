from tkinter import *
import math
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer_var = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_var)
    check_mark.config(text='           ',fg=YELLOW,bg=YELLOW)



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global repeat
    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = SHORT_BREAK_MIN * 60
    repeat += 1
    if repeat % 2 == 0 and repeat<8:
        countdown(SHORT_BREAK_SEC)
        title.config(text="break",fg=RED)
    elif repeat % 2 != 0:
        countdown(WORK_SEC)
        title.config(text="Work",fg=GREEN)
    elif repeat % 8 == 0:
        countdown(LONG_BREAK_SEC)
        title.config(text="Long break",fg=PINK)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    mins = count // 60
    secs = count % 60
    if secs >=0 and secs < 10 :
        secs = "0"+ str(secs)
    if mins >= 0 and mins < 10:
        mins = "0" + str(mins)
    if count >= 0 :
        canvas.itemconfig(canvas_text,text='{}:{}'.format(mins,secs))
        global timer_var
        timer_var = window.after(1000,countdown,count-1)
    else:
        sound = r'mixkit-repeating-arcade-beep-1084.wav'
        playsound(sound)
        timer()
        interval = math.floor(repeat / 2)
        global marks
        marks = ""
        if interval<=4:
            for i in range(0,interval):
                marks += "✅"
                check_mark.config(text=marks)

            print(marks)
            if marks == "✅✅✅✅" and interval == 4:
                filename = r'./01.Taka Takata.mp3'
                playsound(filename)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro technique")
window.config(padx=100,pady=50,bg=YELLOW)

#create canvas for tomato image
canvas = Canvas(width=200,height=300,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,120,image=tomato_img)
canvas_text = canvas.create_text(100,150,text='00:00',fill="white",font=(FONT_NAME,35,"bold"))

#add title, check and buttons
title = Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW,highlightthickness=0)
title.grid(row=0,column=1)
# check_1 = Canvas(width=40, height=40, bg=YELLOW)
# check_button = PhotoImage(file='icons8-check-box-with-check-48.png')
# check_1.create_image(20, 20, image=check_button)
# check_1.grid(row=2, column=2)
check_mark = Label(text=marks, fg="green")
check_mark.grid(row=2, column=1)
start = Button(text='start',padx=10,command=timer)
start.grid(row=2,column=0)
reset = Button(text='reset',padx=10,command=reset_timer)
reset.grid(row=2,column=3)

#need to work using grid method 
canvas.grid(row=1,column=1)
window.mainloop()