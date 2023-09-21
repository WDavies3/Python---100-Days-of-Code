import os
from art import logo

def calculate_winner(bids = {}):
    winner = ""
    largest_bid = 0
    for key,val in bids.items():
        if val > largest_bid:
            winner = key
            largest_bid = val
    return winner

bids = {}
os.system('cls')
print(logo)
print("Welcome to the secret auction")
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    continue_bidding = input('Are there any other bidders? Type "yes" or "no": ')
    os.system('cls')
    if continue_bidding == "yes":
        continue
    else:
        break
winner = calculate_winner(bids)
print(f'The winner is {winner} with a winning bid of ${bids[winner]}')