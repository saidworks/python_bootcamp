import tkinter as tk
import turtle
#create window
window = tk.Tk()
window.title("my first GUI program")
window.minsize(width=500,height=300)

#label
my_label = tk.Label(text="I am a label",font=('Arial',24))
my_label.pack(side="top",expand=0)

tim = turtle.Turtle()
tim.write('some text',font=("Time New Roman",24,"bold"))


#loop to keep screen running
window.mainloop()