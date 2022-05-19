print("Строка:")
string = "The school year usually runs from September to June"
print(string)
unique = []
for char in string[::]:
    if char not in unique:
        unique.append(char)
print("Количество уникальных символов - ", len(unique))
