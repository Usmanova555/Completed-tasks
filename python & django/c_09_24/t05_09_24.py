def flip(func):
    def wrapper(ss):
        func(list(reversed(ss)))
    return wrapper
@flip
def func(ss):
    for i in range(len(ss)): print(ss[i])
l = []
while True:
    str = input()
    if str != '0': l.append(str)
    else: break
print("Вывод в обратном порядке")
func(l)
