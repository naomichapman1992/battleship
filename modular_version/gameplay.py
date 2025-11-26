# gameplay.py - Handles turns, firing, hits/misses, scoring

from state import *
from board import print_single_grid, input_coordinate

def print_grid():
    """
    Displays the current player's board and the opponent's board.
    Own ships are visible; enemy ships stay hidden unless hit.
    """
    attacker = current_player
    defender = 1 - current_player

    print_single_grid("Your Board", player_grids[attacker], reveal_ships=True)
    print_single_grid(f"{player_names[defender]}'s Board", player_grids[defender], reveal_ships=False)


def accept_valid_player_placement():
    """
    Prompts current player to enter a coordinate to shoot.
    Rejects locations already targeted.
    """ 
    defender = 1 - current_player
    target_grid = player_grids[defender]

    while True:
        row, col = input_coordinate("Shoot (e.g. A5): ")

        # Ensure not to shoot the same spot twice
        if target_grid[row][col] in (Cell.HIT, Cell.MISS):
            print("You already shot there, try again.")
            continue

        return row, col


def check_if_ship_sunk(row, col):
    """
    Checks whether a newly hit ship is now fully destroyed.
    If so, increments sunk-ship count.
    """
    defender = 1 - current_player
    grid = player_grids[defender]

    for ship in player_ship_positions[defender]:
        if (row, col) in ship["coords"] and all(grid[r][c] == Cell.HIT for r, c in ship["coords"]):
            print(f"You sank the {ship['name']}!")
            ships_sunk[current_player] += 1
            return


def shoot_bullet():
    """
    Handles one complete firing turn.
    Takes input, marks hit/miss, updates statistics,
    and checks sunk status.
    """
    global player_hits, player_misses, shots_taken

    defender = 1 - current_player
    grid = player_grids[defender]

    print(f"\n--- {player_names[current_player]}'s turn ---")
    print_grid()

    row, col = accept_valid_player_placement()
    cell = grid[row][col]

    shots_taken[current_player] += 1

    if cell == Cell.SHIP:
        print("Hit!")
        grid[row][col] = Cell.HIT
        player_hits[current_player] += 1
        check_if_ship_sunk(row, col)
    else:
        print("Miss.")
        grid[row][col] = Cell.MISS
        player_misses[current_player] += 1


def show_live_score():
    """
    Prints actual scoreboard: hits/misses/sunk per player.
    """
    print("\n--- LIVE SCORE ---")
    for i in (0, 1):
        print(f"{player_names[i]}: {player_hits[i]} hits, {player_misses[i]} misses, {ships_sunk[i]} sunk ship(s)")
    print()


def check_game_over():
    """
    Evaluates whether player has sunk all enemy ships.
    """
    global game_over

    for i in (0, 1):
        if ships_sunk[i] == num_ships:
            print(f"\n{player_names[i]} has destroyed all enemy ships!")
            print(f"{player_names[i]} wins!")
            game_over = True
            return


def switch_player():
    """
    Alternates player turn, prevents board peeking.
    """
    global current_player
    current_player = 1 - current_player
    input("\nPress ENTER and hand over to next player...")
    print("\n" * 50)
