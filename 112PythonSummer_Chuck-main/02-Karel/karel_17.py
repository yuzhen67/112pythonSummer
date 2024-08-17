from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def main():
    """ Karel code goes here! """
    while True:
        if right_is_clear():
            turn_right()
            move()
            if not beepers_present():
                put_beeper()
            turn_around()
            move()
            turn_right()
            move()
        elif front_is_clear() and right_is_blocked():
            move()
        else:
            break
    pass

if __name__ == "__main__":
    run_karel_program('./worlds/fill_pothole2.w')
    #run_karel_program(os.path.join(os.getcwd(), 'worlds/fill_pothole2'))