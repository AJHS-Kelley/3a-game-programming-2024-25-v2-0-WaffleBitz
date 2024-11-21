# Flow Control Structures, Alexander Oropeza-Licona, v0.0
# Making Computer Programs Make Decisions

temperature = 100
color = "Lavender"
height = 5
likes_pineapple_on_pizza = True

# SINGLE DECISION POINT - if STATEMENT
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time.
    # run_this_code IF the CONDITIONAL_EXPRESSION is TRUE.

if temperature > 100:
    print("It is hot as the sun outside!\n")

if likes_pineapple_on_pizza == True:
    print("Mmm! Pineapple on Pizza!\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likes_pineapple_on_pizza:
    print("Yummyz!")

# What if we want something different to happen?
if color == "Lavender": # COMMON MISTAKE FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color.\n")

if likes_pineapple_on_pizza == True:
    print("Give me one slice of pizza please!\n")
else:
    print("I dont what that..\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE 
# Must be > min, height and < max. height to ride.


# When writing if-elif-else blocks check for the HIGHEST value first when using > or >=.
if height >= 6:
    print("You're too tall to ride the Cheese Corpz.\n")
elif height >= 3:
    print("You're tall enough to ride Cheese Cropz.\n")
else: # "oh no, something's wrong!"
    print("Error, Height not detected. Do not ride.\n") 

# When writing if-elif-else blocks check for the LOWEST value first when using < or <=.
if height <= 3:
    print("You're not tall enough to ride the Cheese Corpz.\n")
elif height <= 6:
    print("You're tall enough to ride Cheese Cropz.\n")
else: # "oh no, something's wrong!"
    print("Error, Height not detected. Do not ride.\n")

# Create an if-elif-else block that checks for temperature.
temperature = 100
if temperature >= 100:
    print("it's too hot outside.\n")
elif temperature >= 50:
    print("Recess is allowed.\n")
elif temperature < 50:
    print("Recess is in the GYM.\n")
else: # No Temperature Detected
    print("ERROR\n")




