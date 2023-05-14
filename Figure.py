import turtle
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def draw_figure(self, size, line_color, fill_color):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.circle(size * self.radius)
        turtle.end_fill()


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return 4 * self.side_length

    def draw_figure(self, size, line_color, fill_color):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(size * self.side_length)
            turtle.left(90)
        turtle.end_fill()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def draw_figure(self, color, fill_color):
        t = turtle.Turtle()
        t.color(color)
        t.fillcolor(fill_color)
        t.begin_fill()
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.length)
            t.left(90)
        t.end_fill()


class Triangle:
    def __init__(self, side1, side2, side3, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def get_area(self):
        return 0.5 * self.side1 * self.height

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw_figure(self, color, fill_color):
        t = turtle.Turtle()
        t.color(color)
        t.fillcolor(fill_color)
        t.begin_fill()
        t.forward(self.side1)
        t.left(120)
        t.forward(self.side2)
        t.left(120)
        t.forward(self.side3)
        t.left(120)
        t.end_fill()


class Pentagon:
    def __init__(self, side_length, color="black", fill_color=None):
        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color

    def get_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2

    def get_perimeter(self):
        return 5 * self.side_length

    def draw_figure(self, width=600, height=600):
        turtle.clear()
        turtle.hideturtle()
        turtle.speed(0)
        turtle.color(self.color, self.fill_color)
        turtle.penup()
        turtle.setposition(-width / 2, -height / 2)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(self.side_length)
            turtle.right(72)
        turtle.end_fill()
        turtle.done()


class Hexagon:
    def __init__(self, side_length, color="black", fill_color=None):
        self.side_length = side_length
        self.color = color
        self.fill_color = fill_color

    def get_area(self):
        return 1.5 * math.sqrt(3) * self.side_length ** 2

    def get_perimeter(self):
        return 6 * self.side_length

    def draw_figure(self, width=600, height=600):
        turtle.clear()
        turtle.hideturtle()
        turtle.speed(0)
        turtle.color(self.color, self.fill_color)
        turtle.penup()
        turtle.setposition(-width / 2, -height / 2)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(6):
            turtle.forward(self.side_length)
            turtle.right(60)
        turtle.end_fill()
        turtle.done()
