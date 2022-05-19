class Fib:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1
    def __next__(self):
        if self.a < self.limit:
            t1 = self.a
            t2 = self.b
            self.b += self.a
            self.a = t2
            return t1
        else:
            raise StopIteration
    def __iter__(self):
        return self
s = Fib(int(input("Введите максимальное число - ")))
print(*s)
