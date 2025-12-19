# Python Exercises - Fundamentos de Programação
# Complete Review of All Topics - SOLVED

# ==================== TUPLOS ====================

# Exercise 1: Create a tuple with player coordinates (x, y, z)
# Unpack it and print each coordinate
player_coords = (10, 20, 30)
x, y, z = player_coords
print(f"x = {x}, y = {y}, z = {z}")

# Exercise 2: Create a tuple with student data (name, age, grade, height)
# Try to change the age (this should cause an error - comment it out after trying)
id_student = ("Ana", 20, "Estudante", 1.85, True)
print("Printing 3rd Position:", id_student[3])
# id_student[1] = 21  # TypeError: 'tuple' object does not support item assignment

# Exercise 3: Use slicing to get the first 3 elements of this tuple
game_stats = (100, 50, 25, 10, 5, 2, 1)
print("Slicing the first 3 elements:", game_stats[:3])
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
    for j in range(4):
        row.append(i * 4 + j)
    grid.append(row)
print("4x4 Grid:", grid)
print()

# ==================== FUNÇÕES ====================

# Exercise 6: Create a function that takes a name parameter
# and prints "Hello [name]". Give it a default value of "Player"
def say_hello(name="Player"):
    print("Hello " + name)
say_hello()
say_hello("João")

# Exercise 7: Create a function that receives a number and returns
# both its square and its cube (multiple returns)
def square_and_cube(num):
    return num**2, num**3
result_square, result_cube = square_and_cube(3)
print("Square:", result_square)
print("Cube:", result_cube)

# Exercise 8: Create a function that receives a list and a number
# The function should multiply each element of the list by the number
# and return the modified list
def multiply_list(lst, number):
    return [element * number for element in lst]
my_list = [1, 2, 4, 5]
modified_list = multiply_list(my_list, 5)
print("Modified List:", modified_list)
print()

# ==================== FUNÇÕES RECURSIVAS ====================

# Exercise 9: Create a recursive function to calculate the sum
# of numbers from 1 to n
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
print("Recursive Sum from 1 to 5:", recursive_sum(5))  # 15

# Exercise 10: Create a recursive function to calculate the power
# of a number (base^exponent)
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)
result = power(2, 3)
print(f"2 to the power of 3 is: {result}")
print()

# ==================== SCOPE ====================

# Exercise 11: Create a global variable 'score' with value 0
# Create a function that tries to modify it without using 'global'
# Then fix it using the 'global' keyword
score = 0

def modify_score():
    global score
    score = 10
    print(f"Inside function: {score}")

modify_score()
print(f"Outside function: {score}")

# Exercise 12: Create nested functions where the inner function
# modifies a variable from the outer function using 'nonlocal'
def outer_function():
    count = 0
    
    def inner_function():
        nonlocal count
        count += 1
        print(f"Inner function incremented count to: {count}")
    
    print(f"Starting count: {count}")
    inner_function()
    inner_function()
    print(f"Final count: {count}")

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

# Exercise 14: Create a string "Python Programming"
# Use slicing to extract "Python" and "Programming" separately
text = "Python Programming"
lang = text[:6]
subject = text[7:]
print("Python:", lang)
print("Programming:", subject)

# Exercise 15: Use string methods to:
# - Count how many 'o' letters are in "Hello World"
# - Replace "World" with "Python"
# - Split the string into a list of words
phrase = "Hello World"
print("Number of 'o':", phrase.count('o'))
print("Replace:", phrase.replace("World", "Python"))
print("Split:", phrase.split())
print()

# ==================== DICIONÁRIOS ====================

# Exercise 16: Create a dictionary of 3 games with their release years
# Add a new game, update an existing year, and delete one game
games = {"Elden Ring": 2022, "Halo": 2001, "Pong": 1972}
games["Starfield"] = 2023
games["Halo"] = 2002
del games["Pong"]
print("Games:", games)

# Exercise 17: Create a dictionary where keys are tuples (x, y)
# representing coordinates, and values are room descriptions
map_rooms = {
    (0, 0): "Entrance Hall",
    (0, 1): "Dark Corridor",
    (1, 0): "Treasure Room"
}
print("Room at (0,1):", map_rooms[(0, 1)])

# Exercise 18: Create a nested dictionary representing 2 players
# Each player should have: name, score, level, and inventory (list)
# Iterate through all players and print their information
players = {
    "p1": {"name": "Aris", "score": 50, "level": 5, "inventory": ["Sword", "Potion"]},
    "p2": {"name": "Bob", "score": 80, "level": 7, "inventory": ["Shield", "Bow"]}
}
for pid, info in players.items():
    print(f"Player {info['name']} - Level: {info['level']}, Score: {info['score']}")
    print(f"  Inventory: {info['inventory']}")
print()

# ==================== SETS ====================

# Exercise 19: Create a set with duplicate numbers
# Print it to see that duplicates are removed
my_set = {1, 2, 2, 3, 3, 3}
print("Set (duplicates removed):", my_set)

# Exercise 20: Create two sets of weapons
# Use set operations to find common weapons and unique weapons
w1 = {"Sword", "Bow", "Dagger"}
w2 = {"Bow", "Axe", "Spear"}
print("Common weapons:", w1 & w2)
print("Unique to each:", w1 ^ w2)
print()

# ==================== FUNÇÕES COMO DADOS ====================

# Exercise 21: Create three functions: add10, multiply2, subtract5
# Store them in a dictionary with string keys
# Call each function from the dictionary
def add10(x):
    return x + 10

def multiply2(x):
    return x * 2

def subtract5(x):
    return x - 5

funcs = {
    "add": add10,
    "mult": multiply2,
    "sub": subtract5
}
print("Add 10 to 5:", funcs["add"](5))
print("Multiply 5 by 2:", funcs["mult"](5))

# Exercise 22: Create a function that receives a list and another function
# Apply the function to each element and return the new list
def apply_to_list(lst, func):
    return [func(x) for x in lst]

numbers = [1, 2, 3, 4, 5]
result = apply_to_list(numbers, lambda x: x * 2)
print("Applied function to list:", result)
print()

# ==================== LAMBDAS ====================

# Exercise 23: Create a lambda that checks if a number is even
# Test it with numbers 4 and 7
is_even = lambda x: x % 2 == 0
print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))

# Exercise 24: Use lambda to sort this list of tuples by the second element
scores = [("Ana", 15), ("João", 12), ("Maria", 18), ("Pedro", 14)]
sorted_scores = sorted(scores, key=lambda x: x[1])
print("Sorted by score:", sorted_scores)
print()

# ==================== STACKS ====================

# Exercise 25: Import deque and create a stack
# Push 3 values, then pop 2 values and print them
from collections import deque

stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Remaining stack:", stack)
print()

# ==================== QUEUES ====================

# Exercise 26: Create a queue and enqueue 4 player names
# Dequeue and print them in order
queue = deque()
queue.appendleft("Alice")
queue.appendleft("Bob")
queue.appendleft("Charlie")
queue.appendleft("Diana")
print("Dequeued:", queue.pop())
print("Dequeued:", queue.pop())
print("Remaining queue:", queue)
print()

# ==================== RANDOM ====================

# Exercise 27: Import random and generate:
# - A random float between 0 and 1
# - A random integer between 1 and 100
# - A random choice from a list of weapons
import random

print("Random float:", random.random())
print("Random int (1-100):", random.randint(1, 100))
weapons = ["Sword", "Bow", "Axe", "Spear"]
print("Random weapon:", random.choice(weapons))
print()

# ==================== FICHEIROS ====================

# Exercise 28: Create a text file "test.txt" with 3 lines
# Read all lines and print them
file = open("test.txt", "wt")
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")
file.close()

file = open("test.txt", "rt")
lines = file.readlines()
print("File contents:", lines)
file.close()

# Exercise 29: Append a new line to the file without deleting existing content
file = open("test.txt", "at")
file.write("Line 4 (appended)\n")
file.close()
print()

# ==================== JSON ====================

# Exercise 30: Create a dictionary with game data (name, score, level)
# Save it to a JSON file
# Read it back and print the data
import json

game_data = {"name": "Hero", "score": 1000, "level": 10}

file = open("game.json", "wt")
json_string = json.dumps(game_data)
file.write(json_string)
file.close()

file = open("game.json", "rt")
content = file.read()
loaded_data = json.loads(content)
file.close()
print("Loaded from JSON:", loaded_data)
print()

# ==================== EXCEPÇÕES ====================

# Exercise 31: Create a try-except block that:
# - Tries to convert user input to an integer
# - Catches ValueError if input is not a number
# - Prints an error message
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: That's not a valid number!")

# Exercise 32: Create a custom exception called "InvalidLevelError"
# Raise it when a level is below 1 or above 100
class InvalidLevelError(Exception):
    pass

def set_level(level):
    if level < 1 or level > 100:
        raise InvalidLevelError("Level must be between 1 and 100")
    print(f"Level set to {level}")

try:
    set_level(150)
except InvalidLevelError as e:
    print(f"Error: {e}")
print()

# ==================== ASSERÇÕES ====================

# Exercise 33: Create a function that calculates damage
# Use assert to ensure damage is never negative
def calculate_damage(attack, defense):
    damage = attack - defense
    assert damage >= 0, "Damage cannot be negative"
    return damage

try:
    result = calculate_damage(50, 20)
    print("Damage dealt:", result)
    result = calculate_damage(10, 50)  # This will fail
except AssertionError as e:
    print(f"Assertion failed: {e}")
print()

# ==================== CLASSES ====================

# Exercise 34: Create a class "Player" with attributes:
# name, health, and level
# Create two instances with different values
class Player:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

player1 = Player("Hero", 100, 5)
player2 = Player("Warrior", 120, 7)
print(f"{player1.name} - HP: {player1.health}, Level: {player1.level}")

# Exercise 35: Add a method to the Player class called "take_damage"
# that reduces health by a given amount
class PlayerWithDamage:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage. HP: {self.health}")

player = PlayerWithDamage("Knight", 100, 5)
player.take_damage(25)
print()

# ==================== HERANÇA ====================

# Exercise 37: Create a base class "Item" with attribute "name"
# Create two subclasses: "Weapon" (with damage) and "Armor" (with defense)
class Item:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        print(f"Item: {self.name}")

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
    
    def describe(self):
        print(f"Weapon: {self.name}, Damage: {self.damage}")

class Armor(Item):
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense
    
    def describe(self):
        print(f"Armor: {self.name}, Defense: {self.defense}")

sword = Weapon("Excalibur", 50)
shield = Armor("Steel Shield", 30)
sword.describe()
shield.describe()
print()

# ==================== POLIMORFISMO ====================

# Exercise 40: Create a list with different item types (Weapon, Armor)
# Loop through and call describe() on each
# Each should behave differently based on its class
items = [
    Weapon("Sword", 45),
    Armor("Helmet", 20),
    Weapon("Bow", 35),
    Armor("Chestplate", 50)
]

print("All items:")
for item in items:
    item.describe()
print()

# ==================== EXERCÍCIO INTEGRADO ====================

# Exercise 41-45: Simple text adventure game
class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {"north": None, "south": None, "east": None, "west": None}
    
    def add_exit(self, direction, room):
        self.exits[direction] = room

class GamePlayer:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
    
    def move(self, direction):
        if self.current_room.exits[direction]:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction}.")
            print(self.current_room.description)
        else:
            raise ValueError(f"Cannot go {direction}!")
    
    def save_game(self, filename):
        data = {"name": self.name, "inventory": self.inventory}
        with open(filename, "wt") as f:
            f.write(json.dumps(data))
        print("Game saved!")

# Create rooms
entrance = Room("You are in the entrance hall.")
corridor = Room("You are in a dark corridor.")
entrance.add_exit("north", corridor)
corridor.add_exit("south", entrance)

# Create player
game_player = GamePlayer("Adventurer", entrance)
print(game_player.current_room.description)

# Try moving
try:
    game_player.move("north")
    game_player.move("east")  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")

# Save game
game_player.save_game("savegame.json")