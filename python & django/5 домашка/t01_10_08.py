from math import sqrt

class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def add(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)

    def add2(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def sub2(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(self, m):
        return Vector2D(self.x * m, self.y * m)
    
    def mult2(self, m):
        self.x *= m
        self.y *= m

    def __str__(self):
        return "vector({};{})".format(self.x, self.y)

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def scalar_product(self, vector):
        return self.x * vector.x + self.y * vector.y
    
    def cos(self, vector):
        return self.scalar_product(vector) / (self.length() * vector.length())
    
    def equals(self, vector):
        if self.x == vector.x and self.y == vector.y:
            return True
        return False

