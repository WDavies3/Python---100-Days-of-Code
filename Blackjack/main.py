############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## There is no betting

import os, random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand = []):
    if 11 in hand:
        score = sum(hand)
        if score > 21:
            return score - 10
        else:
            return score
    return sum(hand)

def play_dealers_hand(hand=[]):
    while True:
        score = calculate_score(hand)
        if score == 17 and 11 in hand:
            hand += [random.choice(cards)]
            return hand
        if score > 17:
            return hand
        hand += [random.choice(cards)]
    
    
def deal():
    players_hand = []
    dealers_hand = []
    hit = 'y'
    players_hand += [random.choice(cards)]
    players_hand += [random.choice(cards)]
    dealers_hand += [random.choice(cards)]
    dealers_hand += [random.choice(cards)]
    while hit == 'y':
        players_score = calculate_score(players_hand)
        print(f'Your cards: {players_hand}, current score: {players_score}')
        print(f"Computer's first card: {dealers_hand[0]}")
        if players_score > 21:
            break
        hit = input("Type 'y' to hit.  Type 'n' to stand: ")
        if hit == 'y':
            players_hand += [random.choice(cards)]
    players_score = calculate_score(players_hand)
    print(f'Your final hand: {players_hand}, final score: {players_score}')
    if players_score < 22:
        play_dealers_hand(dealers_hand)
    dealers_score = calculate_score(dealers_hand)
    print(f"Computer's final hand: {dealers_hand}, final score: {dealers_score}")
    if players_score > 21:
        print("You went over 21.  You lose")
    elif players_score > dealers_score:
        print("You win")
    elif players_score == dealers_score:
        print("You and the dealer tied")
    else:
        print("You lose")

while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        break
    os.system('cls')
    print(logo)
    deal()
