from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def climb_up():
    turn_left()
    move()
    turn_right()
    move()
    pass

def climb_down():
    move()
    if right_is_blocked():
        pass
    else:
        turn_right()
        move()
        turn_left()
    pass

def main():
    """ Karel code goes here! """
    while True:
        if beepers_present():
            pick_beeper()
            break
        elif front_is_blocked():
            climb_up()
        elif right_is_blocked() and front_is_clear():
            climb_down()
        else:
            break
if __name__ == "__main__":
    run_karel_program('./worlds/climb.w')
    #run_karel_program(os.path.join(os.getcwd(), 'worlds/climb2'))