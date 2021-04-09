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




#read from csv
''' 
    read from csv 
    compare answer to element from array (row)
    use coordinates to write on the background image 
 '''
states = pd.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title='Guess what is the state', prompt='What is another states name')
    for value in states.iterrows():
        serie = value[1].tolist()
        if answer_state == "exit":
            missing_states = []
            for state in serie:
                if state not in guessed_states:
                    missing_states.append(state)
                    guessed_states.append([i for i in range(50)])
                    break
        if answer_state == serie[0]:
            # define turtle to draw names
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.pu()
            t.goto(int(serie[1]), int(serie[2]))
            t.write(answer_state, align='center')





turtle.mainloop()