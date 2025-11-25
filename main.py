import os
import random

rock = '''
      ________
    /          \\
   /   ______   \\
  /   /      \   \\
  \   \______/   /
   \            /
    \__________/
'''

paper = '''
   ___________________
  |                   |
  |      A4           |
  |                   |
  |___________________|

'''

scissors = '''
      _    _
     ( )  ( )
      \\  //
       \\//
       //\\
      //  \\
     (______)                            
'''

choice = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]

start_system = input("Please Press ENTER To Play the Game! ")
while start_system == "":
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

    os.system("clear")

    player = choice[player_choice]
    computer = random.choice(choice)

    print("PLAYER CHOSE: ")
    print(player)
    print("COMPUTER CHOSE: ")
    print(computer,"\n")

    player_name = names[player_choice]
    computer_name = names[choice.index(computer)]

    if player_name == computer_name:
        print("YOU DRAW")
    elif (player_name == "rock" and computer_name == "scissors") or \
         (player_name == "scissors" and computer_name == "paper") or \
         (player_name == "paper" and computer_name == "rock"):
        print("YOU WIN")
    else:
        print("YOU LOSE")

    retry = input("Wanna Try Again? (Y/N) ").lower()
    if retry == "n":
        break
    elif retry == "y":
        os.system("clear")
    else:
        "System Error, You Typed Wrong!"
        break

print("Have a Nice Day! ~")