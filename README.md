
# Battleship – 2‑Player Console Game
A fully interactive Battleship game built for **Sotwerk AB** coding assignment.  
Players manually place ships or select to havre them randomly placed. The players then take turns firing shots and the game tracks hits, misses & ships sunk live during gameplay.

---

## 🎮 Game Features

| Feature | Supported |
|--------|:---:|
| 10x10 board per player | ✔ |
| Manual ship placement | ✔ |
| Optional Random Ship Placement | ✔ |
| Hit / Miss tracking | ✔ |
| Live Scoreboard | ✔ |
| Win detection on all ships sunk | ✔ |
| Turn‑based alternating play | ✔ |

---

## 🚀 How to Run

Original version:
```bash
python battleship.py
```

Modular enhanced version:
```bash
cd modular_version
python main.py
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

Ships may be placed manually or randomly.

Example manual placement:
```
A5   ← starting coordinate
H/V  ← horizontal or vertical
```

3. Players take turns firing shots at opposing coordinates.
4. The scoreboard updates automatically after every shot.
5. The first player to sink *all enemy ships* wins.

---

## 📊 Live Scoreboard Example

```
--- LIVE SCORE ---
Alice: 3 hits, 2 misses, 1 ship/s sunk  
Bob:   1 hit, 4 misses, 0 ship/s sunk
```

---

## 🏛 Project Structure

### Original Version
```
battleship.py       ← single‑file implementation 
test_battleship.py  ← unit tests
README.md           ← documentation
```

### Modular Version (recommended)
```
modular_version/
│── board.py           ← grid and rendering
│── gameplay.py        ← turns, hits, misses, scoreboard
│── main.py            ← game entry point
│── placement.py       ← manual and random ship placement
│── state.py           ← shared game variables and enums
```

✔ More readable  
✔ Better testability  
✔ Ready for expansion (AI, GUI, networking)

---

## 🔥 Possible Future Enhancements

| Feature | Status |
|---|:---:|
| AI opponent | ☐ |
| Online/network multiplayer | ☐ |
| GUI version | ☐ |
| Save/load games | ☐ |
| Tracking accuracy & stats summary | ☐ |

---

## 🧠 AI Usage Disclosure

AI was used for small productivity boosts, including:

| Contribution | AI Helped |
|---|:---:|
| README formatting & structure | ✔ |
| Modular refactor planning | ✔ |
| Suggestions for code clarity & naming | ✔ |

Core gameplay logic, turn handling, rules, and implementation remain hand‑written.

---

## ⏱ Time Usage Summary

The assignment allowed 8 hours — here is how the time was spent:

| Task | Approx. Time |
|---|:---:|
| Reading rules + YouTube reference | **1–2 hours** |
| Coding (logic, turns, placement, sinking rules) | **4–5 hours** |
| Extra features (random placement, cleanup, comments) | **1 hour** |
| Writing documentation & structure cleanup | **~30 min** |

**Total: ≈ 8 hours**
