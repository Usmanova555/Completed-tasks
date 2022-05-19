num1 = int(input("Введите 1-ое число - "))
num2 = int(input("Введите 2-ое число - "))
len1 = int(len(str(num1)))
len2 = int(len(str(num2)))
res = int(0)
t = num2
for i in range (1,len1+1):
    f1 = num1 % (10**i)
    for j in range (1,len2+1):
        f2 = t % (10**j)
        res += f1*f2
        t -= f2
    num1 -= f1
    t = num2
print(res)
