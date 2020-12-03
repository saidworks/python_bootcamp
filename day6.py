"""https://reeborg.ca fun exercises for functions like turtle """
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
            if not wall_in_front() or not  wall_on_right():
                move()
    elif wall_on_right():
        turn_left()
        move()
    