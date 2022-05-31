'''
Using the turtle module, write a program to draw a house. The house should at least have a roof, a door and some windows. Feel free to play around with the design of your house.
'''

import turtle


def draw_rectangle(color, len1, len2):
    angle = 90
    turtle.color(color)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(len1)
        turtle.right(angle)
        turtle.forward(len2)
        turtle.right(angle)
    turtle.end_fill()


def draw_triangle(color, length):
    angle = 120
    turtle.color(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()


def move_turtle(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()

def draw_house():
    move_turtle(-125,25)
    draw_rectangle('#EF798A', 250, 250)
    draw_triangle('#F7A9A8', 250)
    move_turtle(-100,0)
    draw_rectangle('#613F75', 75, 75)
    move_turtle(25,0)
    draw_rectangle('#613F75', 75, 75)
    move_turtle(-25,-125)
    draw_rectangle('#E5C3D1', 50, 100)
    turtle.done()


draw_house()