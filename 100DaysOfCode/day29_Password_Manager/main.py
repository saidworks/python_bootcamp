from tkinter import *

#----------------UI DEFINITION-----------------#
window = Tk()
window.title('Password Manager')
window.config(padx=100,pady=50,bg='WHITE')

#create canvas for image
canvas = Canvas(width=100,height=100,bg='WHITE',highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,120,img=logo_img)





window.mainloop()
