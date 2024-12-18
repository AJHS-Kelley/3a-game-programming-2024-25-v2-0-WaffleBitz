# Dragon Realm, <Alexander Oropeza>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# 2024-12-09 -- Code Check -- 95%.  Well Done Alex! 
import random # You haven't used this module yet.  If you don't need it, remove this line. 
import time
import datetime 

# SAVING DATA TO A FILE
# STEP 1 -- Create the file name to use.
#log_file_name = "dragon_realm_log" + str(time.time()) + ".txt"
log_file_name = "dragon_realm_log.txt" # Use this line instead of Line 10. 
# Example: dragon_realm_log1132AM.txt

# STEP 2 -- Create / Open the file to save data.
save_data = open(log_file_name, "a")
# FILE MODES
# "x" CREATES FILE, IF EXISTS, EXIT WITH ERROR MESSAGE
# "w" CREATES FILE, IF EXISTS, ERASE AND OVERWRITE FILE CONTENTS
# "a" CREATES FILE, IF EXISTS, APPEND DATA TO THE FILE

save_data.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")

def displayIntro():

    print('You have choose to go up the mountain or toward the forest,')
    print('you are currently in the middle path. the right sign is toward the mountain and the left leads to the forest')
    print('You have a bad feeling about whether this choice will effect your fate.')
    print('Choose Carefully...')
    print()

def choosePath(): # Just figure out which path number.  
    path = ''
    while path != '1' and path != '2':
        print('Which path will you go into? (Mountain = 1 or Forest = 2)')
        path = input()
        if path == '1':
                print('You approach the right side...')
                time.sleep(2)
                print('It is cold and foggy...')
                time.sleep(2)
                print('you then began walking...')
                print()
                time.sleep(2)
        elif path == '2':
                print('You approach the left side...')
                time.sleep(2)
                print('It is dark, damp, and foggy...')
                time.sleep(2)
                print('you then began walking...')
                print()
                time.sleep(2)
        else:
            input("Type in a valid location here and press enter.\n")
            print(choosePath)

def cavePath()-> int:
        print('You have chosen to go up the mountain. In front of you,')
        print('you see two caves. In one cave, the dragon is friendly')
        print('and will share his treasure with you. The other dragon')
        print('is greedy and hungry, and will eat you on sight.')
        print()
        # cave_choice = ''
        while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
        cave = input()
        return cave

def forestPath():
    print("Code not done yet")
# def checkCave(chosenCave):
#     print('You approach the cave...')
#     time.sleep(2)
#     print('It is dark and spooky...')
#     time.sleep(2)
#     print('A large dragon jumps out in front of you! He opens his jaws and...')
#     print()
#     time.sleep(2)

#     friendlyCave = random.randint(1, 2)

#     if chosenCave == str(friendlyCave):
#         print('Gives you his treasure!')

#     else:
#         print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    pathNumber = choosePath()
    if pathNumber == '1': # Mountain
        cavePath()
    elif pathNumber == '2': # Forest
        forestPath()
    # (pathNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# CLOSE THE FILE
save_data.write("END OF GAME LOG\n\n")
save_data.close()