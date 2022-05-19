n = int(input())
arr = []
x = 2*n+1
arr = [[5 for j in range(x)] for i in range(x)]
for i in (arr):
    print(*i)
print()
m = x
l = 0
for i in range (x):
    for j in range (x):
        if ((j>=l) and (j<m)) or ((j-1<l) and (j>=(m-1))):
            arr[i][j] = 0
    l+=1
    m-=1
for i in range (x):
    for j in range (x):
        print(arr[i][j], ' ', end = '')
    print()
