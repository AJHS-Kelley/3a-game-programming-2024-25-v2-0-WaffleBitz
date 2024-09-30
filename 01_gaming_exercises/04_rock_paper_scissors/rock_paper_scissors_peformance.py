# Rock, Paper, Scissors (PEFORMANCE) by Alexander Oropeza-Licona, v0.4

# MODULE IMPORTS
import random, time 

# DATA STRUCTURES -- PLAYER
player_score = 0
player_choice = None
num_draws = 0

# DATA STRUCTURES -- CPU
cpu_score = 0
cpu_choice = None

# MAIN GAME LOOP
while player_score < 5 and cpu_score < 5:

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

    # 1st PLAYER selcet choice at random.
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