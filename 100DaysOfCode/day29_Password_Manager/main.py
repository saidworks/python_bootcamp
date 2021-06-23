from tkinter import *

#----------------UI DEFINITION-----------------#
window = Tk()
window.title('Password Manager')
window.config(padx=100,pady=50,bg='WHITE')

#create canvas for image
canvas = Canvas(width=200,height=300,bg='BLACK',highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,120,image=logo_img)
canvas_text = canvas.create_text(100,150,text='Password Reminder',fill="white",font=('Times New Roman',35,"bold"))
canvas.grid(row=1,column=1)





window.mainloop()
