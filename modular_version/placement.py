# placement.py - Handles manual + random ship placement

import random
from state import *
from board import input_coordinate, print_single_grid

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Attempts to place a ship between two grid points.
    Only allows horizontal or vertical placement.
    Returns True if successfully placed, otherwise False.
    """
    global placing_grid, placing_ship_positions

    # Must be Horizontal or Vertical
    if start_row != end_row and start_col != end_col:
        return False

    coords = []

    # Horizontal
    if start_row == end_row:
        for c in range(start_col, end_col + (1 if end_col > start_col else -1), 
                       1 if end_col > start_col else -1):
            if not (0 <= c < grid_size) or placing_grid[start_row][c] != Cell.EMPTY:
                return False
            coords.append((start_row, c))
    else: # Vertical
        for r in range(start_row, end_row + (1 if end_row > start_row else -1),
                       1 if end_row > start_row else -1):
            if not (0 <= r < grid_size) or placing_grid[r][start_col] != Cell.EMPTY:
                return False
            coords.append((r, start_col))

    # Place ship
    for r, c in coords:
        placing_grid[r][c] = Cell.SHIP

    placing_ship_positions.append(coords)
    return True


def place_ship_randomly(ship_name, ship_len):
    """
    Randomly places a single ship of given length on placing_grid.
    Retries until a valid non-overlapping position is found.
    """
    global placing_grid, placing_ship_positions

    while True:
        direction = random.choice(["H", "V"])
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)

        if direction == "H":
            ok = validate_grid_and_place_ship(row, row, col, col + ship_len - 1)
        else:
            ok = validate_grid_and_place_ship(row, row + ship_len - 1, col, col)

        if ok:
            coords = placing_ship_positions[-1]
            placing_ship_positions[-1] = {"name": ship_name, "coords": coords}
            print(f"✔ {ship_name} placed randomly.")
            break


def create_grid():
    """
    Runs full ship placement for both players.
    Players can choose manual or random placement.
    """
    global player_grids, player_ship_positions, ships_sunk
    global placing_grid, placing_ship_positions

    ships_sunk = [0, 0]

    for player_index, name in enumerate(player_names):
        placing_grid = [[Cell.EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
        placing_ship_positions = []

        print(f"\n--- {name}: Place your ships ---")
        mode = input("Manual or Random? [M/R]: ").strip().upper()
        if mode not in ("M", "R"): mode = "M"

        for ship_name, ship_len in fleet:
            if mode == "R":
                place_ship_randomly(ship_name, ship_len)
                continue

            while True:  
                print_single_grid(
                    f"{name} - Ship layout",
                    placing_grid,
                    reveal_ships=True
                )
                print(f"Place {ship_name}(length: {ship_len})")

                row, col = input_coordinate("Start coordinate (e.g. A5): ")
                direction = input("Direction H/V: ").strip().upper()

                if direction == "H":
                    ok = validate_grid_and_place_ship(row, row, col, col + ship_len - 1)
                else:
                    ok = validate_grid_and_place_ship(row, row + ship_len - 1, col, col)

                if ok:
                    coords = placing_ship_positions[-1]
                    placing_ship_positions[-1] = {"name": ship_name, "coords": coords}
                    print(f"✔ {ship_name} placed!\n")
                    break
                print("Invalid placement - try again.")

        player_grids[player_index] = placing_grid
        player_ship_positions[player_index] = placing_ship_positions

        if player_index == 0:
            input("Player 1 done — pass and press ENTER.")
            print("\n" * 50)

    input("\nBoth players done. Press ENTER to start battle...")
    print("\n" * 50)
