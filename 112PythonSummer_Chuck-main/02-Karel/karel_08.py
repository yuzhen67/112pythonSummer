from stanfordkarel import *
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def climb():
    turn_left()
    move()
    turn_right()
    move()
    pick_beeper()

def main():
    while front_is_blocked():
        climb()
        
    pass

if __name__ == "__main__":
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_08')