class Vector2D:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __get__(self, x, y):
        return x, y

    def __set__(self, x, y, value):
        self.x.value = value
        self.y.value = value

    def add(self, x, y):
        x += self.x
        y += self.y

    def sub(self, x, y):
        x -= self.x
        y -= self.y

    def add2(self, x, y):
        return Vector2D(x + self.x, y + self.y)

    def sub2(self, x, y):
        return Vector2D(x - self.x, y - self.y)

    def mul(self, a, x, y):
        return Vector2D(x*a, y*a)

    def mult2(self, a, x, y):
        x *= a
        y *= a

    def string(self, x, y):
        return x + ';' + y

    def length(self, x, y):
        import math
        math.sqrt(x*x+y*y)

    def scalarProduct(self, x, y):
        return Vector2D(x*self.x, y*self.y)

    def cos(self, x, y):
        import math
        return(x*self.x + y*self.y)/(math.sqrt(x*x+y*y)*math.sqrt(self.x*self.x+self.y*self.y))

    def equals(self, x, y):
        if (x == self.x) and (y == self.y): print('Векторы равны')
        else:
            print('Векторы не равны')

v1 = Vector2D(3.0, 5.2)
print(v1.add(3.2, 4.3))
print(v1.sub(2, 3.0))
print(v1.add2(2.2, 2.5))
print(v1.sub2(3.9, 2.5))
print(v1.length(3, 4))







