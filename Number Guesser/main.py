import random, os
number = random.randint(1,100)
os.system('cls')
print("Guess a Number")
print("The number is between 1 and 100")
level = input("Choose a difficulty.  Type 'easy' or 'hard': ")
attempts_remaining = 0
if level == 'easy':
    attempts_remaining = 10
else:
    attempts_remaining = 5
while attempts_remaining > 0:
    print(f'You have {attempts_remaining} attempts remaining to guess the number.')
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You guessed the number correctly.  Congratulations")
        break
    elif guess > number:
        print("Your guess was too high.  Try again")
    else:
        print("Your guess was too low.  Try again.")
    attempts_remaining -= 1
if attempts_remaining == 0:
    print('You lost.  Rerun the program to try again')
