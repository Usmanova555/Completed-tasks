str = input('Введите текст - ')
s = {}
for i in str:
    if i.isalpha(): 
        if i not in s.keys(): s[i] = 1
        else: s[i] += 1
for key, value in sorted(s.items(), key = lambda item: (item[0].islower(),item[0].isupper(),item[0])):
    print(key, value, sep = ' - ')
