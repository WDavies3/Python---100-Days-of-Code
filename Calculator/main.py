#Command line Calculator App
import os
from art import logo

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1/num2


op_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def intro():
    print(logo)
    num1 = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    return perform_calculation(num1)


def perform_calculation(num1):
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = op_dict[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    return result


while (True):
    os.system('cls')
    num1 = intro()
    while (True):
        choice = input(
            f"Type 'y' to continue calculating with {num1} or type 'n' to start a new calculation: ")
        if choice == 'n':
            break
        if choice == 'y':
            num1 = perform_calculation(num1)
