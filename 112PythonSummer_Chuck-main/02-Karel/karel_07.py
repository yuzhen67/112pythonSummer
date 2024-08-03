from stanfordkarel import *


def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    

 
    pass

if __name__ == "__main__":
    run_karel_program(r'C:\Users\wei\workspace\112PythonSummer_Chuck\02-Karel\worlds\karel_07')