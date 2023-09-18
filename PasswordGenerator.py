#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easyPassword = ''
for x in range(nr_letters):
    easyPassword += letters[random.randint(0,len(letters)-1)]
for x in range(nr_symbols):
    easyPassword += symbols[random.randint(0,len(symbols)-1)]
for x in range(nr_numbers):
    easyPassword += numbers[random.randint(0,len(numbers)-1)]
print(f'Easy Password: {easyPassword}')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hardPassword = ''
hPLetters = []
hPSymbols = []
hPNumbers = []

#build a random list for each of the following letters, symbols, and numbers 
for x in range(nr_letters):
    hPLetters.append(letters[random.randint(0,len(letters)-1)])
for x in range(nr_symbols):
    hPSymbols.append(symbols[random.randint(0,len(symbols)-1)])
for x in range(nr_numbers):
    hPNumbers.append(numbers[random.randint(0,len(numbers)-1)])

#while at least 1 of the lists isn't empty
while(hPLetters or hPSymbols or hPNumbers):
    randList = []
    if hPLetters:
        randList.append(hPLetters)
    if hPNumbers:
        randList.append(hPNumbers)
    if hPSymbols:
        randList.append(hPSymbols)
    randChoice = random.randint(0,len(randList)-1)
    hardPassword += randList[randChoice].pop()
    
print(f'Hard Password, 1st method: {hardPassword}')

#Hard Level - Order of characters randomised: EASIER WAY
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hardPasswordLst = []

#build a random list for each of the following letters, symbols, and numbers 
for x in range(nr_letters):
    hardPasswordLst += random.choice(letters)
for x in range(nr_symbols):
    hardPasswordLst += random.choice(symbols)
for x in range(nr_numbers):
    hardPasswordLst += random.choice(numbers)

random.shuffle(hardPasswordLst)

hardPassword2 = "".join(hardPasswordLst)

print(f'Hard Password, 2nd method: {hardPassword2}')

