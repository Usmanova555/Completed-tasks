s = {}
def func(func):
    def func2(x: int, y: int):
        if (x, y) not in s.keys() and (y,x) not in s.keys():
            s[(x,y)] = func(x,y)
            return s[(x,y)]
        else:
            if (x,y) in s.keys(): return s[(x,y)]
            else: return s[(y,x)]
    return func2
@func
def func3(x1: int, y1: int):
    return x1 * y1
x1 = int(input("Введите 1 число - "))
y1 = int(input("Введите 2 число - "))
print("Результат - " , func3(x1,y1))
