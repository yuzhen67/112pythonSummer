from stanfordkarel import *
# import os
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
def fill_pothole():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()

def main():
    move()
    fill_pothole()
    move()

    """ Karel code goes here! """
    #pass


if __name__ == "__main__":
    # run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_02'))
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_02')
