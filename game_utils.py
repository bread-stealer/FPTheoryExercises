# Create a game_utils.py file which have 5 functions: greetings, class, attack, damage, and enemies life (100)
# Uses inputs in the game loop
# player_class = [“warrior”, ‘mage’, “archer”]
# Base damage (40) with class-based modifier = [1.3, 1.5, 1.2] 

#Player's Classes and their modifiers
player_class = ["warrior", "mage", "archer"]
class_modifiers = {
    "warrior": 1.3,
    "mage": 1.5,
    "archer": 1.2
}

# Base damage and enemy life
base_damage = 40
enemies_life = 100

# Functions

# Greetings function
def greetings():
    print("Enter your name:")
    name = input()
    print(f"Welcome{name}!")

def choose_class():
    # Choose player class
    print("Available classes:", player_class)

    # Player's Input of the chosen class
    print("Choose your class (warrior, mage, archer):")
    chosen_class = input().lower()

    # Printing player's input class
    print("You are a", chosen_class.capitalize(), "with", base_damage, "base damage.")

    # Validation of player's
    print 
    while chosen_class not in player_class:
        print("Invalid class. Please choose again:", player_class)
        chosen_class = input().lower()
    return chosen_class



