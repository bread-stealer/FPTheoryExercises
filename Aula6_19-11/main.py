import game_utils

def main():
    game_utils.greetings()
    player_class = game_utils.choose_class()
    print(f"You have chosen the {player_class} class.")
    # Further game logic can be added here