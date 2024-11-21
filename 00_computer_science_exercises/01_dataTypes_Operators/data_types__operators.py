# Data Types and Operators, Alexander Oropeza-Licona, v0.0

# Fundamental Data Types
# String -- str -- Sequence of letters, numbers, spaces, or other characters.
# Strings in Python are inside '' or ""
# Just be consistent

# Boolean - bool - True or False values. 

# Float - float - any number value with a decimal, +/-, including 0.

# Intergers - int - any whole number, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT!
# VARIABLE CANNOT START WITH A NUMBER
# camelCaseVariableNames
# snake_case_variables_names

# DECLARING VARIABLES AND ASSINGING VALUES

high_score = 6942080085 # int data types

car_speed = 12.55 # float data type, miles per hour

has_axe = True # boolean date type
is_purple = False # boolean date type

player_name = "Alexander Oropeza-Licona" # string data type
power_up = "Drawing Pad" # string data type

# ASSIGN NEW VALUES
player_name = "Wafflebitz" # string data type
car_speed = 3.20

# DATA CAN CHANGE, BE CAREFUL.
has_axe = 5.0

# Printing Data Types
new_int = 3 
new_float = 4.0
new_string = "Cheese Stickz"
new_bool = False

print(type(new_int))
print(type(new_float))
print(type(new_string)) 
print(type(new_bool))

# printing variables to Console / Screen
# print(player_name)
# print(is_purple)
# print(high_score)
# print(car_speed)

# printing variables and expression to console / screen
# print(high_score + 1134)
# print(6 * 7)
# print(high_score)


# PRINTING VARIABLES INSIDE OF STRINGS
# print(f"Hello {player_name}. Congrats! You are a no life witha a high score of {high_score}.\n") 

# ARTTHMETIC OPERATORS
my_int = 26
my_float = 3.41
my_num = 0

# addition
my_int = 9 + 10
my_float = 2.0 + 6.21

my_int = my_int + 5

my_num = my_int + my_float
# When you add an int and a float together, the answer becomes a float

# subtraction
my_num = my_int - my_float
my_int = my_float - 1.25

# Multiplication
my_num = my_int * my_float

# Division
my_num = my_int / my_float # first is numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMING EVEN / ODD NUMBERS.
num_students = 6
num_slices_pizza = 35

left_overs = num_slices_pizza % num_students
# print(left_overs)

# EXPONENTS **
num_squared = 5 ** 2 # 5 is the base, 2 is the exponent.

# FLOOR-DIVISION // -- Divides, THROWS OUT ANY DECIMAL.
my_num = my_int // my_float

# Addition-Assignment Operator - Mostly used for counters.
my_num = 5
my_num = my_num + 1 # Old-School Method
my_num += 1 # New Hotness
my_num *= 1
my_num /= 1


# COMPARISON OPERATORS

# IS-EQUAL-TO -- Are the two values equal to each other?
# Returns True or False based on evaluation.
x = 12.0
# print(x == 5)

# NOT-EQUAL-TO -- Are the two values equal to each other?
# Returns True or False based on evaluation.
# print(x != 12)

# GREATER THAN / GREATER-THAN-OR-EQUAL TO
# print(5 > 3) # Greater Than
# print(12 >= 2) # Greater Than or Equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
# print(5 < 3) # Less Than
# print(12 <= 2) # Less Than or Equal To



# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 22
height = 73.5
eye_color = "dark brown"
# In order to ride the Teacups, you must be at least 18 years old and at least 60" tall.
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eye_color == "dark brown")
# # ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
# # print(defeated_boss == True and level > 5 and has_blue key == True)

# # or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE  STATEMNET TO BE TRUE
# print(age >= 18 or height >= 60)
# print(age >= 18 or height >= 60 or eye_color == "dark brown")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
# print(defeated_boss == True or level > 5 or has_blue key == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 6
print(a == 6)
print(not (not (a == 6)))

# COMBINING LOGICAL OPERATORS
# print(a == 5 and has_key == True or is_cloud == True)
# TRUE and 

# IDENTIFY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATIONS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)
