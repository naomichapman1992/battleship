
# Battleship – 2‑Player Console Game
A fully interactive Battleship game built for **Sotwerk AB** assignment.  
Players manually place ships, take turns firing shots, and the game tracks hits, misses & ships sunk live during gameplay.

---

## 🎮 Game Features

| Feature | Supported |
|--------|:---:|
| 10x10 board per player | ✔ |
| Manual ship placement | ✔ |
| Hit / Miss tracking | ✔ |
| Live Scoreboard | ✔ |
| Win detection on all ships sunk | ✔ |
| Turn‑based alternating play | ✔ |

---

## 🚀 How to Run

```bash
python battleship.py
```

No external dependencies required — Python only.

---

## 📌 Gameplay Overview

1. Both players enter their names.
2. Each player places the following ships:

| Ship | Length |
|------|:-----:|
| Carrier | 5 |
| Battleship | 4 |
| Cruiser | 3 |
| Submarine | 3 |
| Destroyer | 2 |

Ships are placed by entering:

```
A5   ← starting coordinate
H/V ← Horizontal or Vertical
```

3. Players take turns firing shots at opposing grid coordinates.
4. The scoreboard updates automatically after every shot.
5. The first player to sink *all enemy ships* wins.

---

## 📊 Live Scoreboard Displayed in Game

| Player | Hits | Misses | Ships Sunk |
|---|:---:|:---:|:---:|
| Player 1 | dynamic | dynamic | dynamic |
| Player 2 | dynamic | dynamic | dynamic |

Example output after a turn:

```
--- LIVE SCORE ---
Alice: 3 hits, 2 misses, 1 ship/s sunk  
Bob:   1 hit, 4 misses, 0 ship/s sunk
```

---

## 🏁 Win Condition

Game ends immediately when one player sinks all enemy ships.

---

## 📂 File Structure

```
battleship/
│ battleship.py       ← game logic & scoreboard
│ home_assignment.pdf ← instructions
│ README.md           ← you are reading this!
```

---

## 🔥 Future Improvements

| Idea | Status |
|---|:---:|
| AI single‑player mode | ☐ |
| Persistent scoreboard storage | ☐ |
| GUI board (Tkinter / Web) | ☐ |
| Random ship placement option | ☐ |

---

