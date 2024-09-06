# Looooooops, Alexander Oropeza-Licona, v0.0

# TWO TYPES OF LOOPS
# for <-- used when you know how many loops you'll need.
# while <-- used when you do not know how many loops you'll need.

# for loop is like Go Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use a for loop

# # for loop example -- Iterating a List
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for each_fruit in fruits:
#     print(each_fruit)

# # continue Keyword -- Skips the current iteration and then finishes the loop.
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for each_fruit in fruits:
#     if each_fruit == "banana":
#         continue
#     print(each_fruit)

# break Keyword -- Immediately exit the loop.
fruits = ["apple", "banana", "strawberry", "tomato"]
for each_fruit in fruits:
    if each_fruit == "banana":
        break
    print(each_fruit)