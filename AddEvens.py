#Sum all the even numbers from 1-100
#method 1
sum = 0
for x in range(2,101, 2):
    sum += x
print(f'The sum of evens from 1-100 using range stepping is {sum}')

#method 2
total = 0
for x in range(1,101):
    if x%2 == 0:
        total += x
print(f'The sum of evens from 1-100 using modulus is {total}')