from Figure import *
import turtle


# Создание Круга
circle = Circle(50)
print("Площадь круга:", circle.get_area())
print("Длина окружности:", circle.get_perimeter())
circle.drawing_figure("red", "orange", 1)

# Создание Квадрата
square = Square(75)
print("Площадь квадрата:", square.get_area())
print("Периметр квадрата:", square.get_perimeter())
square.drawing_figure("blue", "green", 1)

# Создание Прямоугольника
rectangle = Rectangle(50, 100)
print("Площадь прямоугольника:", rectangle.get_area())
print("Периметр прямоугольника:", rectangle.get_perimeter())
rectangle.drawing_figure("black", "yellow", 1)

# Создание Треугольника
triangle = Triangle(50, 50, 50)
print("Площадь треугольника:", triangle.get_area())
print("Периметр треугольника:", triangle.get_perimeter())
triangle.drawing_figure("purple", "pink", 1)

# Создание Пятиугольника
pentagon = Pentagon(50)
print("Площадь пятиугольника:", pentagon.get_area())
print("Периметр пятиугольника:", pentagon.get_perimeter())
pentagon.drawing_figure("brown", "grey", 1)

# Создание Шестиугольника
hexagon = Hexagon(50)
print("Площадь шестиугольника:", hexagon.get_area())
print("Периметр шестиугольника:", hexagon.get_perimeter())
hexagon.drawing_figure("navy", "skyblue", 1)

# Создание Эллипса
ellipse = Ellipse(50, 100)
print("Площадь эллипса:", ellipse.get_area())
print("Длина периметра эллипса:", ellipse.get_perimeter())
ellipse.drawing_figure("maroon", "violet", 1)

turtle.done()
