from stanfordkarel import *


def walk_and_put_beeper():
    move()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    put_beeper()
    pass

def main():
    put_beeper()
    while front_is_clear():
        walk_and_put_beeper()
    pass

if __name__ == "__main__":
    run_karel_program('7x7')