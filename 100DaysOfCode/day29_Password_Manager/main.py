from tkinter import *

#----------------UI DEFINITION-----------------#
window = Tk()
window.title('Password Manager')
window.config(padx=100,pady=50,bg='WHITE')

#create canvas for image
canvas = Canvas(width=200,height=300,bg='BLACK',highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,120,image=logo_img)
canvas.grid(row=2,column=1)

title = Label(text="Password Manager V1",fg='BLACK',font=('New Times Roman',20,'bold'),bg='WHITE',highlightthickness=0)
title.grid(row=1,column=1)


window.mainloop()
