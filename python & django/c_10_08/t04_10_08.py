from abc import abstractmethod


class Figure:
    def perimeter(self):
        print("Периметр")

    def square(self):
        print("Площадь")

    def print(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    a = 0
    b = 0

    def perimeter(self, a, b):
        super().perimeter()
        return (a + b) * 2

    def square(self, a, b):
        super().square()
        return a * b

    def print(self):
        super().print()
        print('Прямоугольник со сторонами a и b')
        print('Введите сторону a')
        a = int(input())
        print('Введите сторону b')
        b = int(input())


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    r = 0

    def perimeter(self, r):
        super().perimeter()
        import math
        pi = math.pi
        return pi * 2 * r

    def square(self, r):
        super().square()
        import math
        pi = math.pi
        return pi * r * r

    def print(self):
        super().print()
        print('Круг с радиусом r')
        print('Введите радиус r')
        r = int(input())


class Triangle(Rectangle):
    c = 0

    def perimeter(self, a, b, c):
        super().perimeter()
        return a + b + c

    def square(self, a, b, c):
        super().square()
        import math
        return math.sqrt(
            super().perimetr() * (super().perimetr() - a) * (super().perimetr() - b) * (super().perimetr() - c))

    def print(self):
        super().print()
        print('Треугольник со сторонами a, b, c')
        print('Введите строну a')
        a = int(input())
        print('Введите строну b')
        b = int(input())
        print('Введите строну c')
        c = int(input())


class Program(Figure, Rectangle, Circle, Triangle):
    # теперь надо всё это вызвать
    print('Введите количество фигур')
    n = int(input())
    list = [0] * n
    aa = 'rectangle'
    bb = 'circle'
    cc = 'triangle'

    for i in range(n):
        print('Введите название фигуры')
        figure = str(input()).lower()
        if figure == aa:
            list[i] = Rectangle()
            list[i].print()
            print(f'Периметр прямоугольника = {list[i].perimeter()}')
            print(f'Площадь прямоугольника = {list[i].square()}')

        if figure == bb:
            list[i] = Circle()
            list[i].print()
            print(f'Периметр круга = {list[i].perimeter()}')
            print(f'Площадь круга = {list[i].square()}')

        if figure == cc:
            list[i] = Triangle()
            list[i].print()
            print(f'Периметр треугольника = {list[i].perimeter()}')
            print(f'Площадь треугольника = {list[i].square()}')