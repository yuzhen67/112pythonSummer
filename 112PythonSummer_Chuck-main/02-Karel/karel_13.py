from stanfordkarel import *

def fix_the_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

def turn_around():
    turn_left()
    turn_left()

def back_to_bottom():
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def next_column():
    for i in range(4):
        move()

def main():
    while front_is_clear():
        fix_the_column()
        back_to_bottom()
        next_column()
    fix_the_column()
    back_to_bottom()
    pass

if __name__ == "__main__":
    run_karel_program('stone_mason_karel')