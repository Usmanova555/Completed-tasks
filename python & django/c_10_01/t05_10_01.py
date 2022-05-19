from collections import defaultdict 

d = defaultdict(int)

while True:
    s = input()
    if s != '0':
        if tuple(s)[0] not in d.keys():
            d[tuple(s)[0]] = int(tuple(s.replace(', ', ''))[1])
        else:
            d[tuple(s)[0]] += int(tuple(s.replace(', ', ''))[1])
    else:
        break

for key, value in d.items():
    print(key, '-', value)