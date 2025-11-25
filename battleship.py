grid = [[]]
grid_size = 10
num_ships = 8
bullets_left = 50
game_over = False
num_ships_sunk = 0
ship_positions = [[]]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    pass

def try_to_place_ship_on_grid(row, col, direction, ship_length):
    global grid_size
    pass
    return validate_grid_and_place_ship(0, 0, 0, 0)

def create_grid():
    global grid, grid_size, num_ships, ship_positions
    pass
    return try_to_place_ship_on_grid(0, 0, 0, 0)

def print_grid():
    global grid, alphabet
    pass

def accept_valid_player_placement():
    global alphabet, grid
    pass
    return 0, 0

def check_if_ship_sunk(row, col):
    global ship_positions, grid
    pass

def shoot_bullet():
    global grid, num_ships_sunk, bullets_left
    row, col = accept_valid_player_placement()
    pass

def check_game_over():
    global num_ships, num_ships_sunk, bullets_left, game_over
    pass

def main():
    global game_over
    create_grid()
    print_grid()
    while not game_over:
        shoot_bullet()
        check_game_over()
    print("Game Over!")