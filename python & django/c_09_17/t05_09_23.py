n = int(input("Введите размер массива n - "))
list = []
a = 1
print(a)
for i in range(1,n):
    list.append(a)
    if (a>0):
        a = (a+2)*(-1)
    else: a = a*(-1) +2
    print(a)
