def mod_powers(a, n):
    i = 0
    while(True):
        if((a**i) % n == 1 and i != 0):
            yield 1
            break
        yield (a**i) % n
        i += 1
    
for i in mod_powers(int(input()), int(input())):
    print(i)
