#!/usr/bin/python
import turtle

def main():
    window = turtle.Screen()
    emmus = turtle.Turtle()

    make_square(emmus)

    turtle.mainloop()

def make_square(emmus):
# make_line_and_turn(emmus, 100)
    length = int(raw_input("El tamano del cuadro es: "))

    for i in range(4):
        make_line_and_turn(emmus, length)

def make_line_and_turn(emmus, length):
    emmus.forward(length)
    emmus.left(90)

if __name__ == '__main__':
    main()
