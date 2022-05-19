n1, n2 = int(input()), int(input())
def f():
    for x in range(n1):
        x = yield
        print(x)
s = f()
print(next(s))
print(next(s))
s.send(n2)
print(next(s))



