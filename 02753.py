year = int(input())

isLeapYear = 0;

if year % 400 == 0:
    isLeapYear = 1;
elif year % 4 == 0 and year % 100 != 0:
    isLeapYear = 1;

print(isLeapYear)