#1ST EXERCISE

#Creates a system that executes as actions through functions
#Attack, Defend, Cure, Inventory, Flee

actions = {
    "Attack": "You attacked the enemy!",
    "Defend": "You raised your shield!",
    "Cure": "You gained 10 HP!",
    "Inventory": "You opened your inventory.",
    "Flee": "You fleed combat!"
}

def perform_action(action_name):
    action = actions.get(action_name)
    if action:
        return action
    else:
        return "Action not recognized."

print(perform_action("Attack"))
print(perform_action("Defend"))
print(perform_action("Cure"))
print(perform_action("Inventory"))
print(perform_action("Flee"))

#2ST EXERCISE (3rd Exercise)
#Duplicates the actions 2 times
