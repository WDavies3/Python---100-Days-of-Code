def isEven(num):
    return num % 2 == 0


def isOdd(num):
    return num % 2 == 1


def evenOrOdd(num):
    if isEven(num):
        return "Even"
    return "Odd"


print(isEven(24))
print(isEven(25))
print(isOdd(24))
print(isOdd(25))
print(evenOrOdd(24))
print(evenOrOdd(25))
