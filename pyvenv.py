
#SET GAME
#  --------Pseudo code-----------
# 1. Build some set cards with turtle.Pen()
# 2. Build a program creating 9 random set cards and drawing them
# 3.Build some sheets : instructions, game, game over...
#  4. Make the user able to click on cards and control if it's right
# 5. Make a points counter

import turtle
import random


# Display the empty cards
wn = turtle.Screen()


def draw_rect(x_of_card, y_of_card, pen_size):
    pen = turtle.Pen()
    pen.pensize(pen_size)
    pen.turtlesize(0.000001)
    pen.penup()
    pen.goto(x_of_card + 10, y_of_card-10)
    pen.pendown()
    pen.forward(100)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(35)
    pen.penup()


def draw(x, y):
    colors = ("RED", "PURPLE", "GREEN")
    pen = turtle.Pen()
    pen.color(colors[random.randrange(len(colors))])
    pen.pensize(6)
    pen.turtlesize(0.2)
    pen.speed(0)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.forward(120)
    pen.right(90)
    pen.forward(150)
    pen.right(90)
    pen.forward(120)
    pen.right(90)
    pen.forward(150)
    pen.penup()
    shapes = ("rect", "circle", "vague")
    shape = random.choice(shapes)
    shape_sizes = (0.5, 3, 6)
    shape_size = random.choice(shape_sizes)
    numbers = (int(2), int(3), int(3))
    number = numbers[random.randrange(len(numbers))]
    if shape == "rect" and number == int(1):
        draw_rect(x, y, shape_size)
        print("I got one rect")
        if shape == "rect" and number == int(2):
            draw_rect(x, y, shape_size)
            draw_rect(x, y - 40, shape_size)
            print("I got two rects")
        if shape == "rect" and number == int(3):
            draw_rect(x, y, shape_size)
            draw_rect(x, y - 40, shape_size)
            draw_rect(x, y - 80, shape_size)
            print("I got 3 rects")


draw(-260, 260)
draw(-130, 260)
draw(0, 260)
draw(-260, 100)
draw(-130, 100)
draw(0, 100)
draw(-260, -60)
draw(-130, -60)
draw(0, -60)
while True:
    wn.update()
