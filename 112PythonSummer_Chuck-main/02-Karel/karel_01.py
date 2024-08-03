from stanfordkarel import *
# import os
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    # """ Karel code goes here! """
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    move()
    put_beeper()
    move()


    pass

if __name__ == "__main__":
    # run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_01'))
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_01')

# import os

# print("Current working directory:", os.getcwd())
# print("Path to karel_01:", os.path.join(os.getcwd(), 'worlds/karel_01'))
