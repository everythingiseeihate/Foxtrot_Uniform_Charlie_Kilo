import turtle


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.circle(self.radius * size)
        turtle.end_fill()


class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.side * size)
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

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.forward(self.length * size)
        turtle.left(90)
        turtle.forward(self.width * size)
        turtle.left(90)
        turtle.forward(self.length * size)
        turtle.left(90)
        turtle.forward(self.width * size)
        turtle.end_fill()


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def get_perimeter(self):
        return self.a + self.b + self.c

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.forward(self.a * size)
        turtle.left(120)
        turtle.forward(self.b * size)
        turtle.left(120)
        turtle.forward(self.c * size)
        turtle.end_fill()


class Pentagon:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return 0.25 * (5 * (5 + 2 * (5 ** 0.5)) * self.side ** 2) ** 0.5

    def get_perimeter(self):
        return 5 * self.side

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(self.side * size)
            turtle.left(72)
        turtle.end_fill()


class Hexagon:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return 1.5 * 3 ** 0.5 * self.side ** 2

    def get_perimeter(self):
        return 6 * self.side

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return 3.14 * self.a * self.b

    def get_perimeter(self):
        h = ((self.a - self.b) / (self.a + self.b)) ** 2
        return 3.14 * (self.a + self.b) * (1 + 3 * h / (10 + (4 - 3 * h) ** 0.5))

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.left(45)
        for i in range(2):
            turtle.circle(self.a * size, 90)
            turtle.circle(self.b * size, 90)
        turtle.end_fill()
