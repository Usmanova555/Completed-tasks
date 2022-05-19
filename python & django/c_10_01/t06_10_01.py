n = int(input())
def fact(n):
    x, y = 1, 1
    for i in range(n):
        x*=y
        y+=1
        yield x
for x in fact(n):
    print(x, end=' ')
print()
