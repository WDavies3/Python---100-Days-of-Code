def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

print(isLeapYear(2020))
print(isLeapYear(2000))
print(isLeapYear(1900))
print(isLeapYear(1995))