n = int(input("Введите n - "))
m = n
arr = [[0 for j in range(n)] for i in range(n)]
print(arr)
arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i] += [int(input())]
        print(arr) # заполнили массив цифрами
for i in (arr):
    print(*i)
# для побочной диагонали
f = 1
sum = 0
for i in range(n):
    sum += arr[i][n-i-1]
if (sum % 2 != 0): f = 0
if (f==1): print("Сумма элементов побочной диагонали чётна")
else: print("Сумма элементов побочной диагонали нечётна")
# для главной диагонали
f = 1
sum = 0
for i in range(n):
    sum += arr[i][i]
if (sum % 2 != 0): f = 0
if (f==1): print("Сумма элементов главной диагонали чётна")
else: print("Сумма элементов главной диагонали нечётна")
