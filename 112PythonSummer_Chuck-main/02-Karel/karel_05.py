from stanfordkarel import *


def main():
    for i in range(4):
        put_beeper()
        move()
        move()
        move()
        turn_left()

    pass

if __name__ == "__main__":
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_05')
