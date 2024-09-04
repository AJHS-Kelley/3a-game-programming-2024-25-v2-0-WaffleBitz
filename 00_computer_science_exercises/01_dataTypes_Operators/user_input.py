# User Input Practice, Alexander Oropeza-Licona, v.0.0

# input() is the built-in function to get information from the KEYBOARD.
# BASIC EXAMPLE
variable_name = input("Cheese fries.\n") 
print(variable_name)

# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!

# INCORRECT, CAUSES A CONCATENATION ERROR.
# my_number = input("Please type an INTEGER number and press enter.\n")
# print(my_number + 5)

my_number = int(input("26\n"))
print(my_number + 5)

# Wrapper Functions
# int() will convert the data to an INTEGER if possible.
new_number = input("Please type a value and press enter.\n")
print(int(new_number)) # can convert STRING TO INTEGER.
print(float(new_number)) # can convert STRING TO FLOAT.
print(str(new_number)) # can convert INTEGER TO STRING.

# float() will convert the data to a FLOAT if possible.
new_number = input("Please type a value and press enter.\n")
#print(int(new_number)) <-- cannot convert FLOAT TO INTEGER.
print(float(new_number)) # can convert STRING TO FLOAT.
print(str(new_number)) # can convert FLOAT TO STRING.

# str() will convert the data to a STRING if possible.
new_number = 5
print(new_number + new_number) # Should print 10
print(str(new_number + new_number)) # Should print 15