#1st Exercise: Define functions for different actions in a game and execute them.
def attack():
    return "You attacked the enemy!"

def defend():
    return "You raised your shield!"

def cure():
    return "You gained 10 HP!"

def inventory():
    return "You opened your inventory."

def flee():
    return "You flee combat!"

def execute_action(actions):
    return actions()

print("Executing individual actions:", "\n")
print(execute_action(attack))
print(execute_action(defend))
print(execute_action(cure))
print(execute_action(inventory))
print(execute_action(flee))
print("\n")

#2st Exercise: Create a list actions =[] that saves the executed functions
actions = [attack, defend, cure, inventory, flee]

print("Executing actions from the list:", "\n")
for action in actions:
    print(execute_action(action))
print("\n")

#3rd Exercise: Duplicates attack and fleet actions 2 times, cure one time, and inventory doesn't at all.
duplicated_actions = [attack, attack, cure, flee, flee]

print("Executing duplicated actions:", "\n")
for action in duplicated_actions:
    print(execute_action(action))
print("\n")


#5th Exercise: Using a dictionary, create menu that receives the player's input and checks if inputs exists
# and then uses the string functions to clean the input

menu = {
    "a": attack,
    "d": defend,
    "c": cure,
    "i": inventory,
    "f": flee
}

while True:
    user_input = input("Select a command: a, d, c, i, f: ").strip().lower()

    action = menu.get(user_input)
    if action:
        print(execute_action(action), "\n")
    else:
        print("Invalid option.", "\n")