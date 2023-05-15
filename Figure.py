import turtle


class Circle:
    def __init__(self, radius):
        self.radius = radius
        assert isinstance(self.radius, (int, float)), "Ошибка: радиус должен быть числом"
        assert self.radius > 0, "Ошибка: радиус должен быть больше 0"

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
        assert isinstance(self.side, (int, float)), "Ошибка: сторона должна быть числом"
        assert self.side > 0, "Ошибка: сторона должна быть больше 0"

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
        assert isinstance(self.length, (int, float)), "Ошибка: длина должна быть числом"
        assert self.length > 0, "Ошибка: длина должна быть больше 0"
        assert isinstance(self.width, (int, float)), "Ошибка: ширина должна быть числом"
        assert self.width > 0, "Ошибка: ширина должна быть больше 0"

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
        assert isinstance(self.a, (int, float)), "Ошибка: сторона a должна быть числом"
        assert self.a > 0, "Ошибка: сторона a должна быть больше 0"
        assert isinstance(self.b, (int, float)), "Ошибка: сторона b должна быть числом"
        assert self.b > 0, "Ошибка: сторона b должна быть больше 0"
        assert isinstance(self.c, (int, float)), "Ошибка: сторона c должна быть числом"
        assert self.c > 0, "Ошибка: сторона c должна быть больше 0"

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def get_perimeter(self):
        return self.a + self.b + self.c

    turtle.ht()

    def drawing_figure(self, line_color, fill_color, size):
        turtle.ht()
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
        assert isinstance(self.side, (int, float)), "Ошибка: сторона должна быть числом"
        assert self.side > 0, "Ошибка: сторона должна быть больше 0"

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
        assert isinstance(self.side, (int, float)), "Ошибка: сторона должна быть числом"
        assert self.side > 0, "Ошибка: сторона должна быть больше 0"

    def get_area(self):
        return (3 * (3 ** 0.5) * self.side ** 2) / 2

    def get_perimeter(self):
        return 6 * self.side

    def drawing_figure(self, line_color, fill_color, size):
        turtle.pencolor(line_color)
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        for i in range(6):
            turtle.forward(self.side * size)
            turtle.right(60)
        turtle.end_fill()


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        assert isinstance(self.a, (int, float)), "Ошибка: сторона a должна быть числом"
        assert self.a > 0, "Ошибка: сторона a должна быть больше 0"
        assert isinstance(self.b, (int, float)), "Ошибка: сторона b должна быть числом"
        assert self.b > 0, "Ошибка: сторона b должна быть больше 0"

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
