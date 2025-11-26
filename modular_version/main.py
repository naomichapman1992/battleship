# main.py - Entry point. Runs Battleship.

from state import *
from placement import create_grid
from gameplay import shoot_bullet, show_live_score, check_game_over, switch_player

def main():
    """
    Game entry point.
    Sets player names, runs ship placement,
    loops turn-by-turn until one player wins.
    """
    global game_over, current_player

    name1 = input("Name for Player 1: ").strip() or "Player 1"
    name2 = input("Name for Player 2: ").strip() or "Player 2"
    player_names[0] = name1
    player_names[1] = name2

    create_grid()
    game_over = False
    current_player = 0

    while not game_over:
        shoot_bullet()
        show_live_score()
        check_game_over()
        if not game_over:
            switch_player()

    print("Game Over!")

if __name__ == "__main__":
    main()
