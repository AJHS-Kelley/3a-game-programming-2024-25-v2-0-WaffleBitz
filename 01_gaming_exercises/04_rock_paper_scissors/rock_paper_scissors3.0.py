# Rock, Paper, Scissors by Alexander Oropeza-Licona, v3.2

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
def playerName() -> str: # Function Signature -- name of function, (arguments if any)
    """Gets the name from the player and returns it."""
    # The line above is a DOCSTRING, it gives a brief example of what the function does.
    player_name = input("Type in your name here and press enter.\n")
    print(f"Hello {player_name}!\n")
    is_correct = input("Is that correct? Type yes or no and press enter.\n").lower()
    if is_correct == "yes":
        pass
    else:
        player_name = input("Type in your name here and press enter.\n")
    return player_name

# CALLING THE FUNCTION
player_name = playerName()

# THE RULES using MULTI-LINE STRINGS
def rules() -> None:
    """This function prints the rule for rock, paper, scissors."""
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
    # Does another part of this program need to access this imformation?
    # IF YES, YOU MUST HAVE A return STATEMENT
    # IF NO, A return STATEMENT IS NOT REQUIRED

def playerChoice() -> str:
    """Allows the player to chose rock, paper, scissors."""
    player_choice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Please enter rock, paper, or scissors and press enter!").lower()
        if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            print("You are not follwing directions. Please try again.\n")
            exit()  
        print(f"you have chosen {player_choice}.\n")
    else:
        print(f"you have chosen {player_choice}.\n")
        return player_choice
    
def cpuChoice() -> str:
    """Allows the CPU to chose rock, paper, scissors."""
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
    return cpu_choice

def pickWinner(player_choice: str, cpu_choice: str) -> str: # player_choice and cpu_choice are both ARGUMENTS. they will be string values.
    """This function uses the player choice and CPU choice to determine a winner."""
    if player_choice == "rock" and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("The CPU wins a point.\n")
        cpu_score += 1 
        return "CPU Wins."
    # CPU WINS
    elif player_choice == "rock" and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("You win a point.\n")
        player_score += 1
        return "Player Wins."
    # PLAYER WINS
    elif player_choice == "rock" and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("DRAW.\n")
        return "DRAW."
    # DRAW
    elif player_choice == "scissors" and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("The CPU wins a point.\n")
        cpu_score += 1
        return "CPU Wins."
    # CPU WINS
    elif player_choice == "scissors" and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("You win a point.\n")
        player_score += 1
        return "Player Wins."
    # PLAYER WINS
    elif player_choice == "scissors" and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("DRAW.\n")
        return "DRAW."
    # DRAW
    elif player_choice == "paper" and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("The CPU wins a point.\n")
        cpu_score += 1
        return "CPU Wins."
    # CPU WINS  
    elif player_choice == "paper" and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("You win a point.\n")
        player_score += 1
        return "Player Wins."
    # PLAYER WINS
    elif player_choice == "paper" and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        print("DRAW.\n")
        return "DRAW."
    # DRAW
    else:
        print("Unable to determine a WINNER. Please Restart.\n")
        exit()
    # return statements IMMEDIATELY exit a function. 

def score(winner: str) -> int:
    """This function uses the winnerto update the score for CPU, Num, DRAWS, and player score."""
    if winner == "Player Wins":
        score = 1
    elif winner == "CPU Wins":
        score = 1
    else: # This is a DRAW.
        score = 0
    return score



# MAIN GAME LOOP
while player_score < 5 and cpu_score < 5:
    print(f"{player_name} you have {player_score} points.\nThe CPU has {cpu_score} points.\n")
    
  
    # let cpu select choice at random.

# compare player choice to cpu choice
    




print(f"Your Final Score: {player_score} CPU Final Score: {cpu_score}\n")
if player_score > cpu_score:
    print(f"Congratulations! {player_name}, you won!\n")
elif cpu_score > player_score:
    print(f"The CPU Wins.. {player_name}, you bring great shame to your family name.\n") 
else:
    print("Unable to determine a WINNER. Please Restart.\n")