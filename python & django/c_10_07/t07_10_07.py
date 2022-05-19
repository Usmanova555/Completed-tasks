from itertools import product
print(*(''.join(it) for it in product('01', repeat=int(input()))), sep='\n')
