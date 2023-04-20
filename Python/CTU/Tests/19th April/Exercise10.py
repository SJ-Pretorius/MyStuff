import calendar
theyear=int(input('Input the year: '))
themonth=int(input('Input the month: '))
print(calendar.month(theyear, themonth, w=0, l=0))