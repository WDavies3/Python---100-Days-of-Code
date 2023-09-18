#Find the average of a list of numbers
numbers = [98, 80, 77, 42, 20, 60, 88]
#int average
average = sum(numbers)//len(numbers)
print(f'The average with built ins is {average}')

#find average with for loop instead of using sum and len
count = 0
total = 0
for num in numbers:
    count += 1
    total += num
#int avg
newAvg = total // count
print(f'The average without built ins is {newAvg}')