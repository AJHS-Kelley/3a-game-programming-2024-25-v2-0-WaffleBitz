# Rock, Paper, Scissors by Alexander Oropeza-Licona, v0.4

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
player_score = 0
player_name = "Test Player"
player_choice = None

# DATA STRUCTURES -- CPU
cpu_score = 0
cpu_choice = None

# PLAYER NAME INPUT
player_name = input("Type in your name here and press enter.\n")
print(f"Hello {player_name}!\n")
is_correct = input("Is that correct? Type yes or no and press enter.\n").lower()

# .lower() can turn ALL input into lowercase.
# .upper() can turn ALL input into UPPERCASE.

if is_correct == "yes":
    pass
else:
    player_name = input("Type in your name here and press enter.\n")

# THE RULES using MULTI-LINE STRINGS
print("""
Welcome to the Rock, Paper, Scissors Robot!
It's Time To Play ROCK, PAPER, SCISSORS.

You have probably played this thousands of times.. but for those who haven't 
You will select from ROCK, PAPER, SCISSORS. Your Opponent, The CPU, will select from ROCK, PAPER, SCISSORS at random.
First to score 5 points wins
      
1) ROCK BEATS SCISSORS
2) SCISSORS BEATS PAPER
3) PAPER BEATS ROCK
""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of double-quotes is just ignored.
If you need to write large comments, it's easier to use multi-line strings than
putting a # in front of 15 different lines.
"""

# MAIN GAME LOOP
while player_score < 5 and cpu_score < 5:
    print(f"{player_name} you have {player_score} points. \nThe CPU has {cpu_score} points.\n")
    player_choice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if player_choice != "rock" or player_choice != "paper" or player_choice != "scissors":
        player_choice = input("Please enter rock, paper, or scissors and press enter!").lower()
        if player_choice != "rock" or player_choice != "paper" or player_choice != "scissors":
            print("You are not follwing directions. Please try again.\n")
            exit()
            print(f"you have chosen {player_choice}.\n")
    else:
        print(f"you have chosen {player_choice}.\n")

    # print the current score for CPU and Player
    # let player select rock, paper, scissors,
    # let CPU select choice at random.
    # Compare player choice to cpu choice
    # print results to the screen
    # award poiny to winner and output results.