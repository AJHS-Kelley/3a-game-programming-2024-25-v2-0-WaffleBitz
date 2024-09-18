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



if is_correct == "yes":
    pass
else:
    player_name = input("Type in your name here and press enter.\n")