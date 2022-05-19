# 8
print("Размеры массива:")
n = int(input("Введите n - "))
m = int(input("Введите m - "))
k = int(input("Введите k - "))
arr = []
arr=[[[3 for i in range(n)] for j in range(m)] for k in range(k)]
arr1 = []
arr1 = [[0 for i in range(n)] for j in range(m)]
sum = 0
prov = 0
prov1 = 0
R = 0
print()
for z in range (n):
    for i in range (m):
        for j in range (k):
            R = arr[z][i][j]
            arr1[i][j] = R
            if ((R % 3) == 0): sum+=1
        if (sum==k): prov += 1
        sum = 0
    if (prov>0):
       prov1+=1
       prov = 0
if (prov1 == n): 
   print("В каждом двумерном массиве есть такая строка, в которой все элементы делятся на 3")
else:
    print ("Условие не выполнилось")


