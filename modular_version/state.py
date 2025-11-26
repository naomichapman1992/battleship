# state.py - Shared game state + enumerations

from enum import Enum

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
player_hits = [0, 0]
player_misses = [0, 0]
shots_taken = [0, 0]

# Temporary holders while placing ships
placing_grid = None
placing_ship_positions = None
