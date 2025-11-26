# battleship.py - A simple implementation of the Battleship game logic for Sotwerk AB code test.
from enum import Enum
import score_board

# Global variables
grid_size = 10
fleet = [
    ("Carrier", 5),
    ("Battleship", 4),
    ("Cruiser", 3),
    ("Submarine", 3),
    ("Destroyer", 2),
]
num_ships = len(fleet)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Cell(Enum):
    EMPTY = 0        # no ship, not shot
    SHIP = 1         # ship present, not shot
    MISS = -1        # water shot
    HIT = 2          # ship shot

# Per-player state
player_grids = [None, None]            
player_ship_positions = [None, None]
ships_sunk = [0, 0]                    # ships sunk per player
player_names = ["Player 1", "Player 2"]
current_player = 0
game_over = False

# Used during ship placement to know which grid/list to update
placing_grid = None
placing_ship_positions = None

# Reads and validates a coordinate like "A5" and returns (row, col) as 0-based ints.
def input_coordinate(prompt):
    while True:
        text = input(prompt).strip().upper()

        if len(text) < 2:
            print("Invalid format. Use e.g. A5.")
            continue

        col_letter = text[0]
        row_part = text[1:]

        if col_letter not in alphabet[:grid_size]:
            print("Invalid column letter.")
            continue

        try:
            row = int(row_part) - 1
        except ValueError:
            print("Row must be a number.")
            continue

        col = alphabet.index(col_letter)

        if not (0 <= row < grid_size and 0 <= col < grid_size):
            print("Coordinates out of bounds.")
            continue

        return row, col


# Validates and places a ship on the grid if the position is free.
def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    global placing_grid, placing_ship_positions

    # Must be Horizontal or Vertical
    if start_row != end_row and start_col != end_col:
        return False

    coords = []

    # Horizontal ship
    if start_row == end_row:
        for c in range(start_col, end_col + (1 if end_col > start_col else -1), 
                       1 if end_col > start_col else -1):
            if not (0 <= c < grid_size) or placing_grid[start_row][c] != Cell.EMPTY:
                return False
            coords.append((start_row, c))

    # Vertical ship
    else:
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


# Tries to place a ship starting from a position in a direction.
def try_to_place_ship_on_grid(row, col, direction, ship_length):
    # Direction: 0 = horizontal, 1 = vertical
    if direction == 0:
        start_row = row
        end_row = row
        start_col = col
        end_col = col + ship_length - 1
    else:
        start_row = row
        end_row = row + ship_length - 1
        start_col = col
        end_col = col

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


# Creates the grid and initializes per-player state.
def create_grid():
    global player_grids, player_ship_positions, ships_sunk, current_player, game_over

    # New game state
    player_grids = [
        [[Cell.EMPTY] * grid_size for _ in range(grid_size)],
        [[Cell.EMPTY] * grid_size for _ in range(grid_size)]
    ]
    player_ship_positions = [[], []]
    ships_sunk = [0, 0]
    current_player = 0
    game_over = False


# Prints the grid to the console.
def print_grid():
    global grid, alphabet
    print("\n   " + " ".join(alphabet[i] for i in range(grid_size)))

    for r in range(grid_size):
        row_display = []
        for c in range(grid_size):
            cell = grid[r][c]
            if cell == Cell.HIT:
                row_display.append("X")
            elif cell == Cell.MISS:
                row_display.append("O")
            else:
                row_display.append(".")  # hide ships
        print(f"{r+1:2} " + " ".join(row_display))

    print()

# Accepts and validates player input for shooting.
def accept_valid_player_placement():
    global grid
    while True:
        row, col = input_coordinate("Shoot (e.g. A5): ")

        # Make sure we don't shoot the same spot twice
        if grid[row][col] in (Cell.HIT, Cell.MISS):
            print("You already shot there, try again.")
            continue

        return row, col

# Checks if a ship has been fully sunk.
def check_if_ship_sunk(row, col):
    global ship_positions, grid
    pass

# Handles a player's shot.
def shoot_bullet():
    global grid, num_ships_sunk, bullets_left
    row, col = accept_valid_player_placement()
    pass

# Determines if the game is over.
def check_game_over():
    global num_ships, num_ships_sunk, bullets_left, game_over

    if num_ships_sunk == num_ships:
        print("Congratulations! You sank all the ships!")
        game_over = True
    elif bullets_left <= 0:
        print("Out of bullets! Game over, you lose.")
        game_over = True

# Switches to the other player.
def switch_player():
    global current_player
    current_player = 1 - current_player
    input("\nPress ENTER and hand over to the next player...")
    print("\n" * 50)


# Runs the main game loop.
def main():
    global game_over, current_player

    # Optionally ask for names
    name1 = input("Name for Player 1 (leave blank for 'Player 1'): ").strip() or "Player 1"
    name2 = input("Name for Player 2 (leave blank for 'Player 2'): ").strip() or "Player 2"
    player_names[0] = name1
    player_names[1] = name2

    create_grid()
    game_over = False
    current_player = 0

    while not game_over:
        shoot_bullet()
        check_game_over()
        if not game_over:
            switch_player()

    print("Game Over!")

if __name__ == "__main__":
    main()