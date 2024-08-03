from stanfordkarel import *
def put_five_beepers():
    for i in range(5):
        put_beeper()

def move_to_next_corner():
    move()
    move()
    move()
    turn_left()

def main():
    for i in range(4):
        put_five_beepers()
        move_to_next_corner()

    """ Karel code goes here! """
    pass

if __name__ == "__main__":
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_06')