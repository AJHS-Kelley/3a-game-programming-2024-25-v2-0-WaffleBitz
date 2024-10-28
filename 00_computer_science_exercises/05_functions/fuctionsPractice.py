# Functions Practice, Alexander Oropeza-Licona, v0.0

import random

# def helloWorldMulti(): # FUNCTION SIGNATURE
#     """This function will output Hello, World! in a language the user choose. """ # DOCSTRING \
#     # print a list of languages to the screen, at least three but no more than five.
#     print("Hello World! Translator\n The languages avaliable are\n [E]nglish\n [S]panish\n [F]rench\n [I]talian\n Please Choose Your Language of Choice")
#     # allow the user to select (input) a choice for the language.
#     language = input("What language do you want? Please type the first letter of the language you want.\n").upper()
    
#     if language == "E":
#         print("Hello, World!\n")
#     elif language == "S":
#         print("Hola, Mundo!")
#     elif language == "F":
#         print("Bonjour le monde!")
#     elif language == "I":
#         print("Ciao Mondo!")
#     else:
#         print ("Please select a valid letter.")

#     # print "Hello, World!" to the screen in that language.
    
# helloWorldMulti()

# Function to Determine Even / Odd Numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1: int) -> bool: # Requires one ARGUMENT (argument1) and RETURNS a Boolean value.
    """Determines if an interger value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False

print(isEven(argument1)) 

# Function with Multiple Arguments
def canRideRollerCoaster(age: int, hieght: int) -> bool:
    if age > 10 and hieght > 4:
        print("You can ride.\n")
        return
    else:
        print("You cannot ride.\n")
        return False

canRideRollerCoaster(4, 10) # Arguments must be passed in the same order as the function signature indicates.