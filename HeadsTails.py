import random

def flipCoin():
    result = random.randint(0,1)
    return "heads" if result == 0 else "tails"
    

print(flipCoin())