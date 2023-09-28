#Higher Lower Game
#User is presented with two options and picks which one 
#has a higher following on instagram.  If the user is correct
#they get a point and the game continues.  If they are wrong 
#the game is over
from art import logo,vs
from game_data import data
import os, random

def print_choice(choice, which):
    text = "Compare A" if which == 'a' else "Against B"
    print(f"{text}: {choice['name']}, a {choice['description']} from {choice['country']}.")

score = 0
game_over = False
choiceA = random.choice(data)
while not game_over:
    #clear the screen
    os.system('cls')
    #print heading
    print(logo)
    #if the user was right, tell them so and give the score
    if score > 0:
        print(f"You're right! Current score: {score}.")
    #print the first choice
    print_choice(choiceA, 'a')
    #print 'vs'
    print(vs)
    #get the second choice
    choiceB = random.choice(data)
    while choiceA == choiceB:
        choiceB = random.choice(data)
    #print the second choice
    print_choice(choiceB, 'b')
    #get the users guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #get the choice with the largest follower count
    greater_followers = 'a' if choiceA['follower_count'] > choiceB['follower_count'] else 'b'
    #if correct increase the score and reassign choiceA for next loop cycle else end game
    if user_guess == greater_followers:
        score += 1
        choiceA = choiceB
    else:
        game_over = True

#game is over, print final score
print(f"Sorry, that's wrong.  Final score: {score}")
