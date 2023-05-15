from Figure import *
import turtle


# Создание Круга
circle = Circle(100)
print("Площадь круга:", circle.get_area())
print("Длина окружности:", circle.get_perimeter())
circle.drawing_figure("firebrick", "papayawhip", 1)

# Создание Квадрата
square = Square(150)
print("Площадь квадрата:", square.get_area())
print("Периметр квадрата:", square.get_perimeter())
square.drawing_figure("paleturquoise", "springgreen", 1)

# Создание Прямоугольника
rectangle = Rectangle(100, 200)
print("Площадь прямоугольника:", rectangle.get_area())
print("Периметр прямоугольника:", rectangle.get_perimeter())
rectangle.drawing_figure("gainsboro", "palegoldenrod", 1)

# Создание Треугольника
triangle = Triangle(120, 120, 120)
print("Площадь треугольника:", triangle.get_area())
print("Периметр треугольника:", triangle.get_perimeter())
triangle.drawing_figure("fuchsia", "plum", 1)

# Создание Пятиугольника
pentagon = Pentagon(100)
print("Площадь пятиугольника:", pentagon.get_area())
print("Периметр пятиугольника:", pentagon.get_perimeter())
pentagon.drawing_figure("bisque", "cornflowerblue", 1)

# Создание Шестиугольника
hexagon = Hexagon(80)
print("Площадь шестиугольника:", hexagon.get_area())
print("Периметр шестиугольника:", hexagon.get_perimeter())
hexagon.drawing_figure("cyan", "thistle", 1)

# Создание Эллипса
ellipse = Ellipse(100, 200)
print("Площадь эллипса:", ellipse.get_area())
print("Длина периметра эллипса:", ellipse.get_perimeter())
ellipse.drawing_figure("maroon", "lightgoldenrodyellow", 1)

turtle.done()
