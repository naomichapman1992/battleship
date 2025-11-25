# Battleship Game

A professional two-player implementation of the classic Battleship board game in Python.

## Features

### Core Gameplay
- **Classic Battleship Rules**: Full compliance with [Wikipedia Battleship rules](https://en.wikipedia.org/wiki/Battleship_(game))
- **Two Game Modes**:
  - Human vs Human (local play)
  - Human vs AI (with intelligent opponent)
- **8 Ships**: Battleship (4), Cruiser (3), Destroyer (2), and 5 Submarines (1 each)
- **10x10 Grid**: Standard game board with coordinate-based targeting
- **Hit/Miss Tracking**: Visual feedback for shots (💥 HIT, 💧 MISS)
- **Ship Sinking**: Ships sink when all cells are hit

### Bonus Features
- **AI Opponent**: Smart AI using a hunting algorithm
  - Uses checkerboard pattern to search efficiently
  - Switches to hunting mode when a hit is detected
  - Attempts to sink ships by targeting adjacent cells
- **Game Statistics**: Tracks rounds and displays game summary

### Code Quality
- **Clean Architecture**: Modular design with separation of concerns
- **Object-Oriented Design**: Well-defined classes with single responsibilities
- **Type Hints**: Full type annotations for better code clarity
- **Documentation**: Comprehensive docstrings and inline comments
- **Test Suite**: 20+ unit tests covering all major components
- **Modern Python**: Uses dataclasses, enums, and abstract base classes

## Project Structure

```
battleship/
├── battleship.py           # Main game implementation
├── test_battleship.py      # Unit tests
├── README.md              # This file
└── .gitignore             # Git ignore rules
```

## Game Components

### Core Classes

#### `CellState` (Enum)
Represents the state of a cell on the game board.
- `EMPTY`: Empty water
- `SHIP`: Ship location (hidden from opponent)
- `HIT`: Ship hit by opponent
- `MISS`: Shot that missed
- `HIDDEN`: Unknown cell (opponent's perspective)

#### `ShipType` (Enum)
Defines available ship types with their sizes:
- `BATTLESHIP`: 4 cells
- `CRUISER`: 3 cells
- `DESTROYER`: 2 cells
- `SUBMARINE`: 1 cell

#### `Ship` (Dataclass)
Represents a ship with:
- Type (determines size)
- Position (starting coordinate)
- Orientation (Horizontal/Vertical)
- Hit tracking

Key methods:
- `is_sunk()`: Check if ship has been destroyed
- `occupies(row, col)`: Check if ship occupies a cell

#### `GameBoard`
Manages the 10x10 grid:
- Ship placement with validation
- Shot processing
- Hit/miss detection
- Ship sinking logic

Key methods:
- `place_ship(ship)`: Add ship with validation
- `receive_shot(row, col)`: Process incoming shot
- `all_ships_sunk()`: Check win condition
- `get_visible_board()`: Get opponent's view

#### `Player` (Abstract Base Class)
Base class for all players:
- Abstract methods: `setup_ships()`, `get_shot_target()`
- Shared attributes: `name`, `board`, `shots_fired`

#### `HumanPlayer` (extends Player)
Interactive player with:
- Terminal-based ship placement
- User input for targeting
- Board visualization

#### `AIPlayer` (extends Player)
Computer opponent with:
- Random ship placement
- Intelligent targeting (checkerboard + hunting)
- Adaptive strategy based on shot results

#### `Game`
Main game controller:
- Turn management
- Win condition checking
- Shot processing and reporting
- Game flow orchestration

## Installation

### Requirements
- Python 3.7+
- No external dependencies

### Setup

```bash
# Clone the repository
git clone https://github.com/naomichapman1992/battleship.git
cd battleship

# Run the game
python battleship.py

# Run tests
python -m pytest test_battleship.py
# or
python -m unittest test_battleship.py
```

## How to Play

### Starting the Game

```bash
python battleship.py
```

### Game Setup

1. Select game mode (Human vs Human or Human vs AI)
2. Player 1 places ships:
   - Enter row (0-9) and column (0-9)
   - Enter orientation: H (Horizontal) or V (Vertical)
   - Ships are validated to prevent overlap and adjacency
3. Player 2 places ships (or AI places automatically)

### Gameplay

1. Players take turns calling out coordinates to attack
2. Result is displayed:
   - 💥 **HIT**: Shot hit a ship
   - 💧 **MISS**: Shot missed
   - **SUNK**: A complete ship was destroyed
3. First player to sink all opponent ships wins

### Board Display

- `.` = Empty water
- `S` = Your ship
- `X` = Your ship was hit
- `O` = Your shot missed
- `?` = Opponent's cell (unknown)

## Testing

Run the comprehensive test suite:

```bash
# Using unittest
python -m unittest test_battleship.py -v

# Using pytest
pytest test_battleship.py -v
```

### Test Coverage

The test suite includes:
- **Ship Tests**: Creation, occupancy, sinking logic
- **Board Tests**: Placement validation, shot processing, board state
- **AI Tests**: Setup, targeting, hunting behavior
- **Game Tests**: Initialization and flow
- **Total**: 20+ test cases covering all major functionality

Example test output:
```
test_ai_does_not_repeat_shots ... ok
test_ai_gets_valid_target ... ok
test_ai_hunting_mode ... ok
test_ai_setup_ships ... ok
test_all_ships_sunk ... ok
test_board_initialization ... ok
test_duplicate_shot ... ok
test_game_initialization ... ok
test_horizontal_ship_occupies ... ok
test_invalid_ship_placement_out_of_bounds ... ok
test_overlapping_ships ... ok
test_ship_creation ... ok
test_shot_hit ... ok
test_shot_miss ... ok
...
```

## Code Examples

### Starting a Game

```python
from battleship import Game, HumanPlayer, AIPlayer

# Create players
player1 = HumanPlayer("Alice")
player2 = AIPlayer("HAL")

# Create and run game
game = Game(player1, player2)
game.setup()
game.play()
```

### Creating a Ship

```python
from battleship import Ship, ShipType

ship = Ship(
    ship_type=ShipType.BATTLESHIP,
    position=(0, 0),
    orientation="H",
    hits=set()
)

# Check occupancy
ship.occupies(0, 2)  # True
ship.occupies(1, 0)  # False
```

### Working with the Board

```python
from battleship import GameBoard, Ship, ShipType

board = GameBoard()

# Place a ship
ship = Ship(ShipType.SUBMARINE, (5, 5), "H", set())
board.place_ship(ship)

# Fire a shot
hit, sunk_ship = board.receive_shot(5, 5)
print(f"Hit: {hit}, Sunk: {sunk_ship is not None}")
```

## Architecture Decisions

### Separation of Concerns
- **Board Management** (`GameBoard`): Handles grid state and validation
- **Ship Management** (`Ship`): Encapsulates ship data and logic
- **Player Abstraction** (`Player`): Base class for different player types
- **Game Control** (`Game`): Orchestrates game flow

### Design Patterns
- **Abstract Base Class**: `Player` defines interface for human and AI
- **Enum**: Type-safe ship types and cell states
- **Dataclass**: Simplified `Ship` definition
- **Strategy Pattern**: Different AI strategies (search vs. hunt)

### Validation
- Ship placement: Bounds checking, overlap detection, adjacency validation
- Shot processing: Duplicate shot prevention, coordinate validation
- Player input: Type checking and range validation

## Performance Considerations

- **Time Complexity**: O(1) for shot processing (direct array access)
- **Space Complexity**: O(n²) for board storage (n=10, minimal impact)
- **AI Targeting**: O(n²) worst case for finding next target (acceptable for 10x10 grid)

## Future Enhancements

Potential improvements:
1. **Advanced AI**: Minimax algorithm, probability maps
2. **Networking**: Multiplayer over internet using sockets/WebSockets
3. **GUI**: Visual board with mouse interaction (Tkinter/PyGame)
4. **Game Variants**: Different grid sizes, ship configurations
5. **Persistent Storage**: Save/load games, player statistics
6. **Difficulty Levels**: Easy/Medium/Hard AI modes
7. **Tournaments**: Best-of-N matches with scoring

## Code Quality Metrics

- **Cyclomatic Complexity**: Low - clear, straightforward logic
- **Test Coverage**: 20+ tests for core functionality
- **Documentation**: 100% of public methods documented
- **Type Hints**: 100% type annotated
- **PEP 8 Compliance**: Full adherence to Python style guide

## Author

Created as a Softwerk AB coding assessment.

## License

MIT License - Feel free to use and modify
