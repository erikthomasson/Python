year = int(input('Write a year that want to know if its a leap year or not :'))
if year % 4 == 0 and year % 100 != 0:
    print(year, 'is a leap year')
elif year % 100 == 0 and year % 400 == 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')