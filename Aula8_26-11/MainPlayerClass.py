# Main File to run Player Class

from PlayerClass import Player

# Main
name = input("Type your name: ")
player = Player(name, 0, 0, 5)

player.log()

# Dictionary with movement commands
movements = {
    "n": lambda: (0, 1),    # north
    "s": lambda: (0, -1),   # south
    "e": lambda: (1, 0),    # east
    "w": lambda: (-1, 0),   # west
    "ne": lambda: (1, 1),   # northeast
    "nw": lambda: (-1, 1),  # northwest
    "se": lambda: (1, -1),  # southeast
    "sw": lambda: (-1, -1)  # southwest
}

print("\nDirections: n, s, e, w, ne, nw, se, sw")
print("q = quit")

while True:
    print(f"\nCurrent Position -> x: {player.x} y: {player.y}")
    command = input("Move: ").lower().strip()
    
    if command == 'q':
        break
    
    if command in movements:
        if not player.is_exhausted():
            dx, dy = movements[command]()
            player.move(dx, dy)
        else:
            print("Too tired to move")
            break
    else:
        print("Invalid command!")

player.log()