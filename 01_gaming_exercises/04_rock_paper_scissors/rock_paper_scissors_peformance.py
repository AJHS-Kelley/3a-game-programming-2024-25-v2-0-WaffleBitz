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
loop_count = 0
loops_req = int(input("How many loops do you want?\nEnter an interger, no commas, and press ENTER.\n"))
# req is the universal abbreviation in computer programming for REQUEST. reqs = REQUESTS
rps_time_start = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loop_count < loops_req:

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
    player_choice = random.randint(0, 2)# randomly select 0, 1, or 2.
    if player_choice == 0:
        player_choice = "rock"
    elif player_choice == 1:
        player_choice = "paper"
    elif player_choice == 2:
        player_choice = "scissors"
    else: 
        print("Unable to determine CPU choice.. \nPlease restart.\n")
        exit()
# compare player choice to cpu choice
    if player_choice == "scissors" and cpu_choice == "rock":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("The CPU wins a point.\n")
        # cpu_score += 1
        cpu_score = cpu_score + 1
    # CPU WINS
    elif player_choice == "scissors" and cpu_choice == "paper":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("You win a point.\n")
        # player_score += 1
        player_score = player_score + 1
    # PLAYER WINS
    elif player_choice == "rock" and cpu_choice == "scissors":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("DRAW.\n")
        # num_draws += 1
        player_score = player_score + 1
    # DRAW
    elif player_choice == "paper" and cpu_choice == "scissors":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("The CPU wins a point.\n")
        # cpu_score += 1
        cpu_score = cpu_score + 1
    # CPU WINS  
    elif player_choice == "paper" and cpu_choice == "rock":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("You win a point.\n")
        # player_score += 1
        player_score = player_score + 1
    # PLAYER WINS
    elif player_choice == "rock" and cpu_choice == "paper":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("DRAW.\n")
    # DRAW
        # num_draws += 1
        player_score = player_score + 1
    elif player_choice == "rock" and cpu_choice == "rock":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("The CPU wins a point.\n")
        # cpu_score += 1
        num_draws = num_draws + 1
    # CPU WINS
    elif player_choice == "scissors" and cpu_choice == "scissors":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("You win a point.\n")
        # player_score += 1
        num_draws = num_draws + 1
    # PLAYER WINS
    elif player_choice == "paper" and cpu_choice == "paper":
        # print(f"The CPU chose {cpu_choice} and you chose {player_choice}.\n")
        # print("DRAW.\n")
    # DRAW
        # num_draws += 1
        num_draws = num_draws + 1
    else:
        print("Unable to determine a WINNER. Please Restart.\n")
        exit()
    loop_count += 1


print(f"Player Final Score: {player_score} CPU Final Score: {cpu_score}\nDraws: {num_draws}\n")
if player_score > cpu_score:
    print(f"Congratulations! , you won!\n")
elif cpu_score > player_score:
    print(f"The CPU Wins.., you bring great shame to your family name.\n") 
else:
    print("Unable to determine a WINNER. Please Restart.\n")
    exit()

rps_time_stop = time.time()
rps_time = rps_time_stop - rps_time_start
print(f"Number of Loops: {loop_count}\n")
print(f"Execution Time: {rps_time:.2F}\n")
