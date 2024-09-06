# Looooooops, Alexander Oropeza-Licona, v0.0
import random # import the random module for us to use.
# Generally put all your import statements at the top.

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

# # break Keyword -- Immediately exit the loop.
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for each_fruit in fruits:
#     if each_fruit == "banana":
#         break
#     print(each_fruit)

# # for loops using range().  range(x) is Exclusive, it starts at 0 and ends at x - 1
# for i in range(10): #is 0 - 9
#     print(i)

# # Might not always want to start at zero.
# for i in range(100): #
#     print(i)

# # Not want to count by 1 -- RARE
# for i in range(10, 100, 5): # 10 = start, 100 - 1 = stop, 5 = # to count by
#     print(i)

# # Sometimes you're not done writing the loops.
# for x in range(10):
#     pass # tells Python this loops isn't finished, don't freak out.

# while loops -- Musical Chairs
player_score = 0 
counter = 0
while player_score < 100: # Run as long as this is True.
    print(f"Starting: {player_score}")
    player_score += random.randint(1,100)
    print(f"After: {player_score}")
    counter += 1
print (f"Counter: {counter}")