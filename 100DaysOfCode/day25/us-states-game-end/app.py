import turtle
import pandas as pd

# setup screen
screen = turtle.Screen()
screen.title("U.S States Game")
# add background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# #get coordinates of mouse on click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
#get answer from user
answer_state = screen.textinput(title='Guess what is the state', prompt='What is another states name')


#read from csv
states = pd.read_csv("50_states.csv")
state = states.state
for value in state.values:
    if answer_state == value:
        print("ok")

        
print(states.state)
turtle.mainloop()