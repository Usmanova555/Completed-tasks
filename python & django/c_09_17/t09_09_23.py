9 #
s = str(input("Введите строку s - "))
s1 = str(input("Введите строку s1 - "))
j = 0
for i in range (len(s)):
    if (s[i] < s1[j]):
        print("Строка s стоит раньше строки s1")
        break
    elif (s[i] > s1[j]):
        print("Строка s1 стоит раньше строки s")
        break
    else: j+=1
