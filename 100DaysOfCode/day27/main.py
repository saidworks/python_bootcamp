from tkinter import *
import math
#create window
window = Tk()
window.title("Miles <=> Km conversion")
window.minsize(width=200,height=200)

#label
my_label = Label(text="Meters to Miles Conversion",font=('Arial',24))
my_label.pack(side="top",expand=0)

#calculate
def km_to_mile():
    km = input.get()
    miles = round((float(km) * 0.621371),2)
    #result
    result = Label(text=f"{miles} miles",font=("Times New Roman",30,"bold"))
    result.pack(side="bottom",expand=1)
def mile_to_km():
    miles = input.get()
    km = round((float(miles) * 1.60934),2)
    #result
    global result
    result = Label(text=f"{km}km",font=("Times New Roman",30,"bold"))
    result.pack(side="bottom",expand=1)
#buttons
km_button = Button(text="km to mi",command=km_to_mile)
km_button.pack()

mi_button = Button(text="mi to km",command=mile_to_km)
mi_button.pack()

#input
input = Entry()
input_frame = Frame(input,width=200,height=200)
input.pack()

def clear_window():
    result.pack_forget()
    print(result)
clear = Button(text="Clear",command=clear_window)
clear.pack()

#loop to keep screen running
window.mainloop()