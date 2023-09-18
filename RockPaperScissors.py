import random

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
paper = '''
    _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \`\`-.'-._;
   \    '   |
    \  .`  /
     |    |
'''

scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
while (True):
    print('Thank you for playing Rock, Paper, Scissors.')
    choice = input('Choose (R)ock, (P)aper, (S)cissors, or (Q)uit: ')
    choice = choice.lower()
    choiceIsValid = False
    #playerChoice = 0
    match choice[0]:
        case 'r':
            print('You chose Rock')
            print(rock)
            choiceIsValid = True
            #playerChoice = 1
        case 'p':
            print('You chose Paper')
            print(paper)
            choiceIsValid = True
            #playerChoice = 2
        case 's':
            print("You chose Scissors")
            print(scissors)
            choiceIsValid = True
            #playerChoice = 3
        case 'q':
            break
    if choiceIsValid:
       compChoice = random.randint(1,3)
       match compChoice:
              case 1:
                     print('Computer chose Rock')
                     print(rock)
                     if choice == 'r':
                        print("You Tied, Play Again")
                     elif choice == 'p':
                        print("Paper beats Rock.  You Win!!!")
                     elif choice == 's':
                        print("You Lost, Rock beats Scissors.  Try again")
              case 2:
                     print('Computer chose Paper')
                     print(paper)
                     if choice == 'r':
                        print("You Lost, Paper beats Rock.  Try again")
                     elif choice == 'p':
                        print("You Tied, Play Again")
                     elif choice == 's':
                        print("Scissors beats Paper.  You Win!!!")
              case 3:
                     print('Computer chose Scissors')
                     print(scissors)
                     if choice == 'r':
                        print("Rock beats Scissors, You Win!!!")
                     elif choice == 'p':
                        print("You Lost, Scissors beats Paper.  Try again")
                     elif choice == 's':
                        print("You Tied.  Play again")


