# Python Exercises - Fundamentos de Programação
# Complete Review of All Topics

# ==================== TUPLOS ====================

# Exercise 1: Create a tuple with player coordinates (x, y, z)
# Unpack it and print each coordinate
player_coords = (10, 20, 30)
x, y, z = player_coords
print(f"x = {x}, y = {y}, z = {z}")

# Exercise 2: Create a tuple with student data (name, age, grade, height)
# Try to change the age (this should cause an error - comment it out after trying)
id_student = ("Ana", 20, "Estudante", 1.85, True)  # [0, 1, 2, 3, 4]
print("Printing 3rd Position:", id_student[3])

# id_student[1] = 21 # Error because tuples can't be change
# TypeError: 'tuple' object does not support item assignment


# Exercise 3: Use slicing to get the first 3 elements of this tuple
game_stats = (100, 50, 25, 10, 5, 2, 1)
print("Slicing the first 3 elements:", game_stats[:3])
# When slicing, the tuple starts in 1: [1, 2, 3, 4, 5, 6, 7]
print()

# ==================== LISTAS DE LISTAS ====================

# Exercise 4: Create a 3x3 map using nested lists
# Access and print the element at position [1][2]

map = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]

print("Element at position [1][2]:", map[1][2])

# Exercise 5: Create a 4x4 grid dynamically using loops
# Fill it with values from 0 to 15
grid = []
for i in range(4):
    row = []
    for j in range (4):
        row.append(i * 4 + j)
        grid.append(row)
        print("4x4 Grid:", grid)
print()

# ==================== FUNÇÕES ====================

# Exercise 6: Create a function that takes a name parameter
# and prints "Hello [name]". Give it a default value of "Player"
def say_hello(name="Player"):
    print("Function takes a Name Parameter:", "Hello " + name)
say_hello()

# Exercise 7: Create a function that receives a number and returns
# both its square and its cube (multiple returns)
def square(num):
    return num**2, num**3
result_square, result_cube = square(3)
print("Square:", result_square)
print("Cube:", result_cube)

# Exercise 8: Create a function that receives a list and a number
# The function should multiply each element of the list by the number
# and return the modified list
def multiply_list(list, number):
    return [element * number for element in list]

list = [1, 2, 4, 5]
number = 5
modified_list = multiply_list(list, number)
print("Modified List:", modified_list)
print()

# ==================== FUNÇÕES RECURSIVAS ====================

# Exercise 9: Create a recursive function to calculate the sum
# of numbers from 1 to n
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n * recursive_sum(n-1)
print("Recursive Sum from 1 to 5:", recursive_sum(5))
 

# Exercise 10: Create a recursive function to calculate the power
# of a number (base^exponent)
def power(base, exponent):
    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    # Base case: handling power of 1 (optional, but improves efficiency)
    elif exponent == 1:
        return base
    # Recursive step: x^n = x * x^(n-1)
    else:
        return base * power(base, exponent - 1)

result = power(2, 3)
print(f"2 to the power of 3 is: {result}") # Output: 8
print()

# ==================== SCOPE ====================

# Exercise 11: Create a global variable 'score' with value 0
# Create a function that tries to modify it without using 'global'
# Then fix it using the 'global' keyword
score = 0  # Global variable

def global_variable():
    global score  # Links the local name to the global variable
    score = 10    # Modifies the original variable
    print(f"Inside function (local): {score}")

global_variable()
print(f"Outside function (global): {score}")

# Exercise 12: Create nested functions where the inner function
# modifies a variable from the outer function using 'nonlocal'
def outer_function():
    # This variable is in the nonlocal scope
    count = 0
    
    def inner_function():
        nonlocal count  # Tells Python to use the 'count' from outer_function
        count += 1
        print(f"Inner function incremented count to: {count}")
        
    print(f"Starting outer count: {count}")
    inner_function()
    inner_function()
    print(f"Final outer count: {count}")

outer_function()
print()

# ==================== STRINGS ====================

# Exercise 13: Take user input, clean it with .strip() and .lower()
# Check if it's empty and print an appropriate message
user_input = input("Enter something: ").strip().lower()
if not user_input:
    print("The input is empty!")
else:
    print(f"Cleaned input: {user_input}")
print()

# Exercise 14: Create a string "Python Programming"
# Use slicing to extract "Python" and "Programming" separately
text = "Python Programming"
lang = text[:6]         # "Python"
subject = text[7:]      # "Programming"
print("Prints Only Python:", lang)
print("Prints Only Programming:", subject)

# Exercise 15: Use string methods to:
# - Count how many 'o' letters are in "Hello World"
# - Replace "World" with "Python"
# - Split the string into a list of words
phrase = "Hello World"
print("Number of Os in the word:", phrase.count('o')) # 2
print("Replaces World for Python:", phrase.replace("World", "Python"))
print("Splits the strings into a list:", phrase.split()) # ['Hello', 'World']


# ==================== DICIONÁRIOS ====================

# Exercise 16: Create a dictionary of 3 games with their release years
# Add a new game, update an existing year, and delete one game
games = {"Elden Ring": 2022, 
         "Halo": 2001, 
         "Pong": 1972}

games["Starfield"] = 2023        # Add
games["Halo"] = 2002             # Update
del games["Pong"]                # Delete

# Exercise 17: Create a dictionary where keys are tuples (x, y)
# representing coordinates, and values are room descriptions
map_rooms = {
    (0, 0): "Entrance Hall",
    (0, 1): "Dark Corridor"
}
# Exercise 18: Create a nested dictionary representing 2 players
# Each player should have: name, score, level, and inventory (list)
# Iterate through all players and print their information
players = {
    "p1": {"name": "Aris", "score": 50, "inventory": ["Sword"]},
    "p2": {"name": "Bob", "score": 80, "inventory": ["Shield"]}
}
for pid, info in players.items():
    print(f"Player {info['name']} (Score: {info['score']})")
print()
# ==================== SETS ====================

# Exercise 19: Create a set with duplicate numbers
# Print it to see that duplicates are removed
my_set = {1, 2, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

# Exercise 20: Create two sets of weapons
# Use set operations to find common weapons and unique weapons
w1 = {"Sword", "Bow"}
w2 = {"Bow", "Axe"}
print(w1 & w2) # Common: {'Bow'}
print(w1 ^ w2) # Unique: {'Sword', 'Axe'}
print()

# ==================== FUNÇÕES COMO DADOS ====================

# Exercise 21: Create three functions: add10, multiply2, subtract5
# Store them in a dictionary with string keys
# Call each function from the dictionary
funcs = {
    "add": lambda x: x + 10,
    "mult": lambda x: x * 2,
    "sub": lambda x: x - 5
}
print(funcs["add"](5)) # 15

# Exercise 22: Create a function that receives a list and another function
# Apply the function to each element and return the new list


# ==================== LAMBDAS ====================

# Exercise 23: Create a lambda that checks if a number is even
# Test it with numbers 4 and 7

# Exercise 24: Use lambda to sort this list of tuples by the second element
scores = [("Ana", 15), ("João", 12), ("Maria", 18), ("Pedro", 14)]


# ==================== STACKS ====================

# Exercise 25: Import deque and create a stack
# Push 3 values, then pop 2 values and print them

from collections import deque


# ==================== QUEUES ====================

# Exercise 26: Create a queue and enqueue 4 player names
# Dequeue and print them in order


# ==================== RANDOM ====================

# Exercise 27: Import random and generate:
# - A random float between 0 and 1
# - A random integer between 1 and 100
# - A random choice from a list of weapons

import random
print(random.random())           # Float 0-1
print(random.randint(1, 100))    # Int 1-100
print(random.choice(["A", "B"])) # Choice


# ==================== FICHEIROS ====================

# Exercise 28: Create a text file "test.txt" with 3 lines
# Read all lines and print them

# Exercise 29: Append a new line to the file without deleting existing content


# ==================== JSON ====================

# Exercise 30: Create a dictionary with game data (name, score, level)
# Save it to a JSON file
# Read it back and print the data

import json


# ==================== EXCEPÇÕES ====================

# Exercise 31: Create a try-except block that:
# - Tries to convert user input to an integer
# - Catches ValueError if input is not a number
# - Prints an error message

# Exercise 32: Create a custom exception called "InvalidLevelError"
# Raise it when a level is below 1 or above 100


# ==================== ASSERÇÕES ====================

# Exercise 33: Create a function that calculates damage
# Use assert to ensure damage is never negative


# ==================== CLASSES ====================

# Exercise 34: Create a class "Player" with attributes:
# name, health, and level
# Create two instances with different values

# Exercise 35: Add a method to the Player class called "take_damage"
# that reduces health by a given amount

# Exercise 36: Create a constructor (__init__) for the Player class
# that initializes all attributes


# ==================== HERANÇA ====================

# Exercise 37: Create a base class "Item" with attribute "name"
# Create two subclasses: "Weapon" (with damage) and "Armor" (with defense)

# Exercise 38: Override a method in the subclass
# Create a method "describe()" in Item that prints the name
# Override it in Weapon to also print damage

# Exercise 39: Use super() in a subclass constructor
# Call the parent constructor and add new attributes


# ==================== POLIMORFISMO ====================

# Exercise 40: Create a list with different item types (Weapon, Armor)
# Loop through and call describe() on each
# Each should behave differently based on its class


# ==================== EXERCÍCIO INTEGRADO ====================

# Exercise 41-45: Create a simple text adventure game that uses:
# - Classes for Room and Player
# - Dictionaries for room connections
# - Functions for movement
# - Exception handling for invalid moves
# - File I/O to save/load game state

# This is your final challenge combining all concepts!
