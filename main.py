from Figure import Circle, Square, Rectangle, Triangle, Pentagon, Hexagon
import turtle

# создание экземпляра класса Circle
circle = Circle(5)

# расчет и вывод площади и периметра круга
print("Circle area:", circle.get_area())
print("Circle perimeter:", circle.get_perimeter())

# отрисовка круга с помощью черепашьей графики
turtle.speed(1)
circle.draw_figure(2, "blue", "green")

# создание экземпляра класса Square
square = Square(10)

# расчет и вывод площади и периметра квадрата
print("Square area:", square.get_area())
print("Square perimeter:", square.get_perimeter())

# отрисовка квадрата с помощью черепашьей графики
turtle.penup()
turtle.setpos(0, -100)
turtle.pendown()
square.draw_figure(1.5, "red", "yellow")

# Создаем прямоугольник со сторонами 4 и 6
rect = Rectangle(4, 6)

# Выводим площадь и периметр прямоугольника
print("Площадь прямоугольника: ", rect.get_area())
print("Периметр прямоугольника: ", rect.get_perimeter())

# Рисуем прямоугольник с черной линией и красной заливкой
rect.draw_figure("black", "red")

# Создаем треугольник со сторонами 3, 4, 5 и высотой 2.5
tri = Triangle(3, 4, 5, 2.5)

# Выводим площадь и периметр треугольника
print("Площадь треугольника: ", tri.get_area())
print("Периметр треугольника: ", tri.get_perimeter())

# Рисуем треугольник с зеленой линией и желтой заливкой
tri.draw_figure("green", "yellow")

# Создаем экземпляр класса Pentagon
pentagon = Pentagon(side_length=100, color="red", fill_color="yellow")

# Выводим площадь и периметр
print("Pentagon area:", pentagon.get_area())
print("Pentagon perimeter:", pentagon.get_perimeter())

# Рисуем пятиугольник
pentagon.draw_figure()

# Создаем экземпляр класса Hexagon
hexagon = Hexagon(side_length=100, color="blue", fill_color="green")

# Выводим площадь и периметр
print("Hexagon area:", hexagon.get_area())
print("Hexagon perimeter:", hexagon.get_perimeter())

# Рисуем шестиугольник
hexagon.draw_figure()

turtle.done()