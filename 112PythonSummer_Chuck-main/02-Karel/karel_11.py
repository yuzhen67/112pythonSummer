from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def main():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    
    
    pass

if __name__ == "__main__":
    run_karel_program('collect_newspaper_karel')