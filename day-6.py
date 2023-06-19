#Solution to 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()

counter = 1
    
while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
        counter += 1
    elif front_is_clear():
        move()
        counter += 1
    else:
        turn_left()
        if front_is_clear():
            move()
            counter += 1
        else:
            turn_left()
            counter += 1

    
