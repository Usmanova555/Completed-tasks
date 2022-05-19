n = int(input())
m = int(input())
print()
arr = [list(map(int, input().split())) for i in range(n)]
arr = sorted(arr, key = lambda k: sum(k))
for i in arr:
    print(*i)
