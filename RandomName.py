import random

def getName(names=[]):
    return names[random.randint(0, len(names)-1)]

def getName2(names=[]):
    return random.choice(names)

strNames = input("Enter a list of names seperated by commas: ")
lstNames = strNames.split(", ")
print(f"The randomly selected name is {getName(lstNames)}")
print(f"The second name is {getName2(lstNames)}")
