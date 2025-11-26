# score_board.py - Handles saving, loading & displaying the Battleship scoreboard.

FILE = "scoreboard.txt"


# Loads and returns scoreboard as {player_name: wins}
def load_scores():
    scores = {}
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for line in f:
                if ":" not in line:
                    continue
                name, wins = line.strip().split(":")
                scores[name] = int(wins)
    except FileNotFoundError:
        pass  # no file yet
    return scores


# Saves all scores to disk
def save_scores(scores):
    with open(FILE, "w", encoding="utf-8") as f:
        for name, wins in scores.items():
            f.write(f"{name}:{wins}\n")


# Increments win count for a player and persists change
def add_win(name):
    scores = load_scores()
    scores[name] = scores.get(name, 0) + 1
    save_scores(scores)


# Prints scoreboard to the terminal
def show_scores():
    scores = load_scores()
    print("\n------ SCOREBOARD ------")
    if not scores:
        print("No scores recorded yet.")
    else:
        for name, wins in sorted(scores.items(), key=lambda x: (-x[1], x[0])):
            print(f"{name}: {wins} win(s)")
    print()
