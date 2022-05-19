def my_filter(more_than: int, elements: list):
    ret = [i for i in elements if i > more_than]
    return ret

ar = []
more_than = int(input())
while(True):
    s = int(input())
    if s != 0:
        ar.append(s)
    else:
        break

for i in my_filter(more_than, ar):
    print(i)