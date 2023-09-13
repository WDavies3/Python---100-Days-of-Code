def combine_digits(num):
    strNum = str(num)
    total = 0
    for digit in strNum:
        total += int(digit)
    return total

print(combine_digits(28))
print(combine_digits(12))
print(combine_digits(26))