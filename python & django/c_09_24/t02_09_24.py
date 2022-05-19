def fib(n):
    a = 0
    b = 1
    while a < n:
        t1 = a
        t2 = b
        b += a
        a = b
        yield t1
print("Введите максимальное число")
print(*fib(int(input())))
