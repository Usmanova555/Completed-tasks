n = int(input("Введите n - "))
m = int(input("Введите m - "))
arr = [[0 for j in range(m)] for i in range(n)]
print(arr)
print("Введите массив")
arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i] += [int(input())]
        print(arr)
for i in (arr):
    print(*i)
print()
for i in range (n-1):
    for i in range(n-1):
        if sum(arr[i])>sum(arr[i+1]):
            k = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = k
for i in arr:
    print(*i)
