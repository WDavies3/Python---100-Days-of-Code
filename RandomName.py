import random

def getName(names=[]):
    return names[random.randint(0, len(names)-1)]

strNames = input("Enter a list of names seperated by commas: ")
lstNames = strNames.split(", ")
print(f"The randomly selected name is {getName(lstNames)}")