import csv
import math
import sys
from datetime import datetime
from datetime import timedelta

dates = []
hours = {}

x = 1000
totalCount = 0

with open("../Resources/ddd.csv", newline='') as csf:
    data = csv.reader(csf, quotechar='|')
    for row in data:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
        except:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")

        totalCount += 1

        hourIndex = date.hour * date.day * date.month * date.year

        if not hours.__contains__(hourIndex):
            hours[hourIndex] = 1
        else:
            hours[hourIndex] = hours[hourIndex] + 1

        dates.append(date)

def getL():
    total = 0
    for key in hours:
        total += hours[key]
    return total / 8760

n = 8
m = sys.maxsize

t = 2.3
T = 30 / 3600

u = 3600 * (1 / t)
l = getL()
p = l / u
a = n / p
b = l * T
c = math.exp(b*(1-a))

def getP0():
    sum = 0
    for k in range(n + 1):
        sum += (math.pow(p, k) / math.factorial(k))

    if p != n:
        B = (c-1)/(1-a)
    else:
        B = 1 + b

    return 1 / (sum + (math.pow(p, n) / math.factorial(n)) * B)

p0 = getP0()
pOTK = (math.pow(p, n) / math.factorial(n)) * c * p0
Q = 1 - pOTK
lIFF = l * Q
lOTK = l * pOTK

def GetW0():
    if p != n:
        D = (a - c*(a*b*(a-1))) / (b*(a-1)*(a-1))
    else:
        D = 1 + b / 2

    return T * (math.pow(p, n) / math.factorial(n)) * D * p0

W0 = GetW0()
k = lIFF / u
L0 = W0 * lIFF
Lc = L0 * k
Wc = Lc / lIFF
fine = pOTK * totalCount * x

print("Cредняя интенсивность потока заявок:", l)
print("Процент необработанных заявок:", pOTK * 100)
print("Среднее время, которое заявка находится в очереди:", W0)
print("Cредняя сумма от штрафов за месяц:", fine / 12)

def total_seconds(date):
    year = int(date.year)
    month = int(date.month)
    day = int(date.day)
    hour = int(date.hour)
    minute = int(date.minute)
    second = int(date.second)
    microsecond = int(date.microsecond)

    delta = timedelta(
        days=year * 365 + month * 12 + day,
        hours=hour,
        minutes=minute,
        seconds=second,
        microseconds=microsecond
    )

    return delta.total_seconds()
