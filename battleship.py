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

    # If both row and col change → diagonal = not allowed
    if start_row != end_row and start_col != end_col:
        return False

    coords = []

    # Horizontal movement
    if start_row == end_row:
        rng = range(start_col, end_col + (1 if end_col > start_col else -1), 
                    1 if end_col > start_col else -1)

        for c in rng:
            if c >= grid_size or placing_grid[start_row][c] != Cell.EMPTY:
                return False
            coords.append((start_row, c))

    # Vertical movement
    else:
        rng = range(start_row, end_row + (1 if end_row > start_row else -1),
                    1 if end_row > start_row else -1)

        for r in rng:
            if r >= grid_size or placing_grid[r][start_col] != Cell.EMPTY:
                return False
            coords.append((r, start_col))

    # Place the ship
    for r, c in coords:
        placing_grid[r][c] = Cell.SHIP

    placing_ship_positions.append(coords)
    return True


# Tries to place a ship starting from a position in a direction.
def try_to_place_ship_on_grid(row, col, direction, ship_length):
    global grid_size
    pass
    return validate_grid_and_place_ship(0, 0, 0, 0)

# Creates the grid and places all ships.
def create_grid():
    global grid, grid_size, num_ships, ship_positions

    # Create an empty grid
    grid = []
    for row in range(grid_size):
        new_row = []
        for col in range(grid_size):
            new_row.append(Cell.EMPTY)
        grid.append(new_row)

    # Reset ship positions
    ship_positions = []

    # Call ship placement function
    for i in range(num_ships):
        try_to_place_ship_on_grid(0, 0, 0, 3)  # Example values for now

    return grid


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

# Runs the main game loop.
def main():
    global game_over
    create_grid()
    print_grid()
    while not game_over:
        shoot_bullet()
        check_game_over()
    print("Game Over!")

if __name__ == "__main__":
    main()