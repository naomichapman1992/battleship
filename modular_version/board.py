# board.py - Handles grid display + coordinate input formatting

from state import alphabet, grid_size, Cell

def input_coordinate(prompt):
    """
    Reads a user-entered coordinate like 'A5',
    validates its format and board boundaries,
    and returns (row, col) as 0-indexed integers.
    """
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


def print_single_grid(title, grid, reveal_ships: bool):
    """
    Prints a grid with column letters and row numbers.
    Shows ship positions only if reveal_ships=True.
    Marks hits as X and misses as O.
    """
    print(f"\n{title}")
    print("   " + " ".join(alphabet[i] for i in range(grid_size)))

    for r in range(grid_size):
        row_display = []
        for c in range(grid_size):
            cell = grid[r][c]

            if cell == Cell.HIT:
                row_display.append("X")   # shot & hit
            elif cell == Cell.MISS:
                row_display.append("O")   # shot but water
            elif reveal_ships and cell == Cell.SHIP:
                row_display.append("S")   # show own ships
            else:
                row_display.append(".")   

        print(f"{r+1:2} " + " ".join(row_display))
    print()
