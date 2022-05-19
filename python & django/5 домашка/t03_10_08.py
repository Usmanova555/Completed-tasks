import math

class Figure:
    def find_area(self):
        raise NotImplementedError()

    def find_perimeter(self):
        raise NotImplementedError()


class PrintableFigureMixin:
    def print(self):
        if issubclass(self.__class__, Figure):
            print(self.__class__.__name__)
        else: print('')         

class Rectangle(Figure, PrintableFigureMixin):
    
    def __init__(self, a, b):
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else: raise Exception("Rectangle can't exist")
    
    def find_area(self):
        return self.a * self.b
    
    def find_perimeter(self):
        return 2 * (self.a + self.b)

class Circle(Figure, PrintableFigureMixin):
    
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return math.pi * self.radius**2

    def find_perimeter(self):
        return self.radius * 2 * math.pi

class Triangle(Figure, PrintableFigureMixin):
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else: raise Exception("Triangle can't exist")
    
    def find_area(self):
        return 0.25 * math.sqrt((self.a+self.b+self.c)*(self.b+self.c-self.a)*(self.a+self.c-self.b)*(self.a+self.b-self.c))

    def find_perimeter(self):
        return self.a + self.b + self.c


figures = [Rectangle(4,5), Circle(5), Triangle(4,3,5)]

for i in figures:
    i.print()
    print(i.find_area())
    print(i.find_perimeter())
    print('***************')