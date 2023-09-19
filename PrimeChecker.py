def isPrime(num):
    if num < 2:
        return False
    for x in range(2,num//2 + 1):
        if num%x==0:
            return False
    return True

for x in range(100):
    print(f'{x}: {"Is prime" if isPrime(x) else "Is not Prime"}')
