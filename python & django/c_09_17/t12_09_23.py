s = str(input("Введите строку на английском языке - "))
prov = 1
ctr = 0
item = ''
for item in s.split():
    prov = 0
    for ch in item:
        if (ch >= 'A' and ch <= 'Z'):
           prov = 1
    if (prov == 1): ctr += 1
print ("Количество слов, которые начинаются на заглавную английскую буквы: ", ctr)
