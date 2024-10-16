# Rock, Paper, Scissors by Alexander Oropeza-Licona, v3.0

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
def playerName(): # Function Signature -- name of function, (arguments if any)
    player_name = input("Type in your name here and press enter.\n")
    print(f"Hello {player_name}!\n")
    is_correct = input("Is that correct? Type yes or no and press enter.\n").lower()

    # .lower() can turn ALL input into lowercase.
    # .upper() can turn ALL input into UPPERCASE.

    if is_correct == "yes":
        pass
    else:
        player_name = input("Type in your name here and press enter.\n")
    return player_name

# CALLING THE FUNCTION
playerName()

# THE RULES using MULTI-LINE STRINGS
print(f"""
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
    print(f"{player_name} you have {player_score} points.\nThe CPU has {cpu_score} points.\n")
    player_choice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Please enter rock, paper, or scissors and press enter!").lower()
        if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            print("You are not follwing directions. Please try again.\n")
            exit()  
        print(f"you have chosen {player_choice}.\n")
    else:
        print(f"you have chosen {player_choice}.\n")

    # let cpu select choice at random.
    cpu_choice = random.randint(0, 2)# randomly select 0, 1, or 2.
    if cpu_choice == 0:
        cpu_choice = "rock"
    elif cpu_choice == 1:
        cpu_choice = "paper"
    elif cpu_choice == 2:
        cpu_choice = "scissors"
    else: 
        print("Unable to determine CPU choice.. \nPlease restart.\n")
        exit()
    # print(f"CPU Choice: {cpu_choice}")

# compare player choice to cpu choice
    if player_choice == "rock" and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("The CPU wins a point.\n")
        cpu_score += 1
    # CPU WINS
    elif player_choice == "rock" and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("You win a point.\n")
        player_score += 1
    # PLAYER WINS
    elif player_choice == "rock" and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("DRAW.\n")
    # DRAW
    elif player_choice == "scissors" and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("The CPU wins a point.\n")
        cpu_score += 1
    # CPU WINS
    elif player_choice == "scissors" and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("You win a point.\n")
        player_score += 1
    # PLAYER WINS
    elif player_choice == "scissors" and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("DRAW.\n")
    # DRAW
    elif player_choice == "paper" and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("The CPU wins a point.\n")
        cpu_score += 1
    # CPU WINS  
    elif player_choice == "paper" and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("You win a point.\n")
        player_score += 1
    # PLAYER WINS
    elif player_choice == "paper" and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("DRAW.\n")
    # DRAW
    else:
        print("Unable to determine a WINNER. Please Restart.\n")
        exit()




print(f"Your Final Score: {player_score} CPU Final Score: {cpu_score}\n")
if player_score > cpu_score:
    print(f"Congratulations! {player_name}, you won!\n")
elif cpu_score > player_score:
    print(f"The CPU Wins.. {player_name}, you bring great shame to your family name.\n") 
else:
    print("Unable to determine a WINNER. Please Restart.\n")