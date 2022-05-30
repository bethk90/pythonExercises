import turtle


def draw_rectangle(color, len1, len2, angle):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(len1)
        turtle.right(angle)
        turtle.forward(len2)
        turtle.right(angle)
    turtle.end_fill()


def draw_triangle(color, length, angle):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()


def move_turtle(len1, len2, angle1, angle2, angle3):
    turtle.pu()
    turtle.right(angle1)
    turtle.forward(len1)
    turtle.right(angle2)
    turtle.forward(len2)
    turtle.right(angle3)
    turtle.pd()


def draw_house():
    turtle.speed(3)
    draw_rectangle('red', 100, 100, 90)
    draw_triangle('yellow', 100, 120)
    move_turtle(20, 20, 0, 90, 270)
    draw_rectangle('blue', 25, 25, 90)
    move_turtle(40, 0, 0, 0, 0)
    draw_rectangle('blue', 25, 25, 90)
    move_turtle(80, 0, 90, 0, 180)
    draw_rectangle('green', 30, 20, 270)
    turtle.done()


draw_house()