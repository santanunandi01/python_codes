import turtle
import tkinter
from tkinter import *


def circle1():
    t.clear()
    t.circle(100)
    t.hideturtle()


def rectangle1():
    t.clear()
    t.forward(150)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.hideturtle()


def square1():
    t.clear()
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.hideturtle()


def triangle1():
    t.clear()
    t.forward(150)
    t.left(120)
    t.forward(150)
    t.left(120)
    t.forward(150)
    t.hideturtle()
    t.left(120)


def hexagon():
    t.clear()
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(60)
    t.hideturtle()


def pentagon():
    t.clear()
    t.forward(150)
    t.left(72)
    t.forward(150)
    t.left(72)
    t.forward(150)
    t.left(72)
    t.forward(150)
    t.left(72)
    t.forward(150)
    t.left(72)
    t.hideturtle()


def clear1():
    t.clear()


root = tkinter.Tk()
root.resizable(0,0)
root.title('The Geometry Shapes')
canvas = tkinter.Canvas(master=root, height=550, width=550)
canvas.pack(side=tkinter.RIGHT)
f = Frame(root)


t = turtle.RawTurtle(canvas)
t.pencolor("Red")
t.pensize(1)
t.penup()
t.pendown()

Label(
    tkinter.Button(master=root, text="circle", command=circle1).pack(fill="both")
)


Label(
    tkinter.Button(master=root, text="rectangle", command=rectangle1).pack(fill="both")
)

Label(
    tkinter.Button(master=root, text="Square", command=square1).pack(fill="both")
)


Label(
    tkinter.Button(master=root, text="Triangle", command=triangle1).pack(fill="both")
)


Label(
    tkinter.Button(master=root, text="Pentagon", command=pentagon).pack(fill="both")
)


Label(
    tkinter.Button(master=root, text="hexagon", command=hexagon).pack(fill="both")
)


Label(
    tkinter.Button(master=root, text="Clear", command=clear1).pack(fill="both")
)

Label(
    tkinter.Button(master=root, text='Quit', command=root.quit).pack(fill="both")
)


root.mainloop(0)
