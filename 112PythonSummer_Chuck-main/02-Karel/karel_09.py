from stanfordkarel import *

def invert_beeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

def main():
    while front_is_clear():
        invert_beeper()
        move()
    invert_beeper()
    pass

if __name__ == "__main__":
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_09')