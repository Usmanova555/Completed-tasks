n = int (input("Введите число n - "))
print ("Введите n цифр")
s1 = ''
for i in range (n):
    f = str(input())
    s1 += f 
print(s1)
s2 = ''
for j in range (1,n+1):
    s2 += s1[-1]
    s1 = s1[0:-1]
print(s2)
