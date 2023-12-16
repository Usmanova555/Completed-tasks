import csv
import sys
from datetime import datetime
from datetime import timedelta

dates = []
minD = sys.maxsize

with open("../Resources/ddd.csv", newline='') as csf:
    data = csv.reader(csf, quotechar='|')
    for row in data:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
        except:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")



        dates.append(date)

def GetMD(list):
    sum1 = 0
    sum2 = 0
    for key in list:
        sum1 += int(key) * list[key]
        sum2 += list[key]

    m = sum1 / sum2

    sum3 = 0
    for key in list:
        sum3 += int(key) * int(key) * list[key]

    d = sum3 / sum2 - m * m

    return m, d

def Get1(month):
    global minD

    lDates = []

    lastDay = -1
    dayCount = 0

    for date in dates:
        if date.month == month:
            if lastDay != date.day:
                dayCount += 1
                lastDay = date.day
            if dayCount <= 3:
                lDates.append(date)

    hours = {}

    for date in lDates:
        hourIndex = (date.hour + (date.day - 1) * 24) + 1
        if not hours.__contains__(hourIndex):
            hours[hourIndex] = 1
        else:
            hours[hourIndex] = hours[hourIndex] + 1

    m, d = GetMD(hours)

    if d < minD:
        minD = d

    print(m, d)

def Get2(month):
    global minD

    lDates = []

    for date in dates:
        if date.month == month:
            lDates.append(date)

    days = {}

    for date in lDates:
        dayIndex = date.day
        if not days.__contains__(dayIndex):
            days[dayIndex] = 1
        else:
            days[dayIndex] = days[dayIndex] + 1

    m, d = GetMD(days)

    m /= 24
    d /= 24

    if d < minD:
        minD = d

    print(m, d)

def Get3(month):
    global minD

    lDates = []

    for date in dates:

        if date.month == month - 1 or date.month == month or date.month == month + 1:
            lDates.append(date)

    weeks = {}

    for date in lDates:
        if not weeks.__contains__(date.weekday()):
            weeks[date.weekday()] = []
        weeks[date.weekday()].append(date)

    for keyWeek in weeks:
        weekDays = {}
        for date in weeks[keyWeek]:
            dayIndex = date.day + date.month * 31
            if not weekDays.__contains__(dayIndex):
                weekDays[dayIndex] = 1
            else:
                weekDays[dayIndex] = weekDays[dayIndex] + 1

        m, d = GetMD(weekDays)

        m /= 24
        d /= 24

        if d < minD:
            minD = d

        print(m, d)

def Get4(month):
    global minD

    lDates = []

    for date in dates:
        if date.month == month - 1 or date.month == month or date.month == month + 1:
            lDates.append(date)

    weeks = {}

    for date in lDates:
        index = int((date.day + date.month * 31) / 7)
        if not weeks.__contains__(index):
            weeks[index] = 1
        else:
            weeks[index] = weeks[index] + 1

    m, d = GetMD(weeks)

    m /= 24
    d /= 24

    if d < minD:
        minD = d

    print(m, d)

def Get5():
    global minD

    months = {}

    for date in dates:
        index = date.month
        if not months.__contains__(index):
            months[index] = 1
        else:
            months[index] = months[index] + 1

    m, d = GetMD(months)

    m /= 24
    d /= 24

    if d < minD:
        minD = d

    print(m, d)

def get_result(month):
    Get1(month)
    Get2(month)
    Get3(month)
    Get4(month)
    Get5()

get_result(8)

print("Средняя интенсивность: ", minD)