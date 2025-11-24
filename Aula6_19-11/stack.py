#1st Exercise: Simulate an actions history of a player in a RPG game.
#Each action is added to the top of the history stack and if the player wants to undo an action, the last action is removed from the stack.

from collections import deque

actions = deque()

list_of_actions = ["walk","attack", "heal", "undo", "exit"]
command = ""

while command != "exit":
    command = input("Action: walk/attack/heal/undo/exit: ").strip().lower()
    
    if command not in list_of_actions:
        print("Invalid action. Try again.")
        continue

    if command == "undo":
        if actions:
            last_action = actions.pop()
            print(f"Undid action: {last_action}")
        else:
            print("No actions to undo.")
        
    if command == "exit":
        actions.append(command)
        print("Action:", command, "registered")

print("\nFinal actions history:", list(actions))


enemies = deque(["goblin", "orc", "troll"])

while enemies:
    actual_enemy = enemies.pop()

    print("Combat with:" , actual_enemy, "is starting!")
    print("Enemy:", actual_enemy, "defeated!\n")