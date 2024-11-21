# Awarding Extra Lives, Alexander Oropeza-Licona, v0.0


lives = 3
# score = 10001
# name = "Alex"

# print(f"Hello {name}! You scored {score} points.\n")


# CHARACTER REFERENCE
# CURLY BRACES {}
# BRACKETS []
# ANGLES-BRACKETS <>
# PARENTHESIS ()

# Allow the user to input the score as an interger.
#The program should output the updated number of lives, and the points scored, as a formatted string.

score = int(input("Enter Score here.\n"))
# if score is 10000 or less
#     Lose a life
# if score is 10000 but less than 100001
#     Give 1 Extra Life
# if score is > 100000
#     Give 2 Extra Lives

# Output the score and number of lives to the screen.

if score <= 10000:
    lives -= 1
    print("-1up\n") # Lose a life
elif score < 100001:
    lives += 1
    print("+1up\n") # Give 1 Extra Life
elif score > 100000: # Give 2 Extra Lives
    lives += 2
    print("+2ups\n") # can convert INTEGER TO STRING.

print("Lives: " + str(lives))
print("Score: " + str(score))