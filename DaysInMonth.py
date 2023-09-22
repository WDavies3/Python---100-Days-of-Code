#returns the number of days in a month, considers whether or not
#the year is a leap year.
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = month_days[month-1]
    if month == 2 and isLeapYear(year):
        days += 1
    return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)