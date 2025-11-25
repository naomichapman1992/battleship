# battleship.py - A simple implementation of the Battleship game logic for Sotwerk AB code test.

grid = []
grid_size = 10
fleet = [5, 4, 3, 3, 2] # lengths of ships - Carrier, Battleship, Cruiser, Submarine, Destroyer
num_ships = len(fleet)
bullets_left = 50
game_over = False
num_ships_sunk = 0
ship_positions = [[]]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

from enum import Enum

class Cell(Enum):
    EMPTY = 0        # no ship, not shot
    SHIP = 1         # ship present, not shot
    MISS = -1        # water shot
    HIT = 2          # ship shot


# Validates and places a ship on the grid if the position is free.
def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    pass

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
    pass

# Accepts and validates player input for shooting.
def accept_valid_player_placement():
    global alphabet, grid
    pass
    return 0, 0

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