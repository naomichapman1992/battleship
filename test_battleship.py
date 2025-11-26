import battleship
from battleship import Cell

def setup_game_state():
    """Reset game state and pre-place two simple ships for testing."""
    battleship.player_grids = [
        [[Cell.EMPTY for _ in range(battleship.grid_size)] for _ in range(battleship.grid_size)],
        [[Cell.EMPTY for _ in range(battleship.grid_size)] for _ in range(battleship.grid_size)]
    ]

    battleship.player_ship_positions = [
        [{"name": "Destroyer", "coords": [(0,0),(0,1)]}],  # Player 1 ship
        [{"name": "Destroyer", "coords": [(5,5),(5,6)]}]   # Player 2 ship
    ]
    battleship.ships_sunk = [0,0]
    battleship.player_hits = [0,0]
    battleship.player_misses = [0,0]
    battleship.current_player = 0


def test_hit_detection():
    setup_game_state()

    defender = 1  # Player 2 is target
    grid = battleship.player_grids[defender]

    # simulate a hit
    grid[5][5] = Cell.SHIP
    battleship.check_if_ship_sunk(5,5)

    assert grid[5][5] == Cell.SHIP  # not sunk yet
    assert battleship.ships_sunk[0] == 0


def test_ship_sinks_after_all_hits():
    setup_game_state()

    defender = 1
    grid = battleship.player_grids[defender]
    ship = battleship.player_ship_positions[defender][0]["coords"]

    # Mark full ship as hit
    for r,c in ship:
        grid[r][c] = Cell.HIT

    battleship.check_if_ship_sunk(ship[0][0], ship[0][1])

    assert battleship.ships_sunk[0] == 1  # Player 1 sunk Player 2 ship


def test_score_updates():
    setup_game_state()

    defender = 1
    grid = battleship.player_grids[defender]
    
    # hit
    grid[5][5] = Cell.SHIP
    battleship.player_hits[0] += 1

    # miss
    grid[2][2] = Cell.EMPTY
    battleship.player_misses[0] += 1

    assert battleship.player_hits[0] == 1
    assert battleship.player_misses[0] == 1
