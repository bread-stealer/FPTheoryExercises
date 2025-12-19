# MATRIX PROPAGATION PROGRAM
# A matrix where activating a cell turns its entire row and column to True.


# Matrix Building
def build_matrix(rows, cols, matriz):
    for r in range(rows):
        matriz.append([])
        for c in range(cols):
            matriz[r].append(False)
    return matriz


# Activate Cell
def activate_cell(row, col, matriz):
    matriz[row][col] = True
    return matriz


# Propagate Activation
def prop_activ(matriz):
    new_matriz = [row.copy() for row in matriz]
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            if matriz[r][c] == True:
                # Fill the entire row
                for col in range(len(matriz[r])):
                    new_matriz[r][col] = True
                # Fill the entire column
                for row in range(len(matriz)):
                    new_matriz[row][c] = True
    return new_matriz


# Minimum Moves Calculator
def min_moves(size):
    return size


# Interactive Game
def interactive_game():
    matriz = build_matrix(4, 4, [])
    
    while True:
        print("\nCurrent Matrix:")
        for row in matriz:
            print(row)
        
        user_input = input("\nEnter row and column to activate or 'quit' to exit: ")
        
        if user_input.lower() == "quit":
            break
        
        try:
            row, col = map(int, user_input.split())
            activate_cell(row, col, matriz)
            propagated = prop_activ(matriz)
            
            print("\nPropagated Matrix:")
            for row in propagated:
                print(row)
            
            activated_count = sum(row.count(True) for row in propagated)
            print(f"\nActivated Cells Count: {activated_count}")
            
        except (ValueError, IndexError):
            print("Invalid input.")
    
    print("\nBye Bye")


# Main execution
if __name__ == "__main__":
    # Display minimum moves info
    size = 4
    print(f"Minimum moves to fill a {size}x{size} matrix: {min_moves(size)}\n")
    
    # Start the game
    interactive_game()
