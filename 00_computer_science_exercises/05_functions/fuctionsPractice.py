# Functions Practice, Alexander Oropeza-Licona, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose. """ # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    print("Hello World! Translator\n The languages avaliable are\n [E]nglish\n [S]panish\n [F]rench\n [I]talian\n Please Choose Your Language of Choice")
    # allow the user to select (input) a choice for the language.
    language = input("What language do you want? Please type the first letter of the language you want.\n").upper()
    
    if language == "E":
        print("Hello, World!\n")
    elif language == "S":
        print("Hola, Mundo!")
    elif language == "F":
        print("Bonjour le monde!")
    elif language == "I":
        print("Ciao Mondo!")
    else:
        print ("Please select a valid letter.")

    # print "Hello, World!" to the screen in that language.
    
helloWorldMulti()

