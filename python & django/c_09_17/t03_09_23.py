num = int(input("Введите число - "))
x = str(num)
length = len(x) # длина строки
digit = int(input("Введите цифру - "))
res = 0
for i in range (1,length+1):
    a = num % (10**i)
    res += a*digit
    num -= a
print(res) 
