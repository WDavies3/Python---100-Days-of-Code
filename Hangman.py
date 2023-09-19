import random, os, Hangman_Art
from Hangman_Words import word_list

def print_word(letters, word):
    display = ""
    for c in word:
        if c in letters:
            display += c
        else:
            display += '_'
    print(display)
    solved = not '_' in display
    return solved

def print_remaining_letters(letters):
    display = ""
    for c in letters:
        display += c
        display += ' '
    print(display)

mistakes = 0
letters = []
remaining_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = random.choice(word_list)
while mistakes < 6:
    os.system('cls')
    print(Hangman_Art.hangman_logo)
    print(Hangman_Art.hangman_image[mistakes])
    if print_word(letters, word):
        break
    print("Letters Remaining:")
    print_remaining_letters(remaining_letters)
    selected_letter = input("Pick a letter\n")[0].lower()
    if selected_letter in remaining_letters:
        remaining_letters.remove(selected_letter)
        if selected_letter in word:
            letters += selected_letter
        else:
            mistakes += 1
    else:
        print("Your selection is not valid.  Try again.")
        
    
    
os.system('cls')
print(Hangman_Art.hangman_logo)
print(Hangman_Art.hangman_image[mistakes])
print_word(letters, word)
if mistakes < 6:
    print("You Win!!!")
else:
    print("You Lose.  Try again.")