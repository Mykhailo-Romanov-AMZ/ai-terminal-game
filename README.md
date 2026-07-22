# Score with Messi

A terminal-based Python game where Messi tries to score all the goals in the universe. Navigate a 5x5 grid, collect footballs to rack up your score, and avoid hazards — all from the comfort of your command line.

## Story

> Messi tries to score all the goals in universe.

You control the star ⭐ on a 5x5 grid. Footballs ⚽ spawn randomly — collect 10 to win. But watch out for 💀 lurking on the grid. Step on one and it's game over.

## Features

- **WASD Movement** — Navigate the grid with classic WASD keys (W=up, A=left, S=down, D=right)
- **Collectible Scoring** — Pick up ⚽ to increase your score; reach 10 to win
- **Random Hazards** — 💀 tiles spawn in random positions; hit one and the game ends
- **Boundary Collision** — Movement is clamped to the grid — no falling off the edge
- **Win/Lose Messages** — Custom end-game messages for victory and defeat
- **Play Again** — After a game ends, choose to restart or exit cleanly
- **Intro Screen** — Game displays its name and story before starting

## How to Run

### Play the Game

```bash
python game.py
```

### Run the Tests

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

## Project Structure

```
.
├── game.py          # Main game logic and loop
├── test_game.py     # Pytest test suite (21 tests)
└── README.md        # This file
```

## What I Learned

- **Iterative Development** — The game was built step by step: grid first, then movement, then collectibles, then hazards, then the play-again loop. Each feature was added only after the previous one was working and tested. This made debugging far easier than trying to build everything at once.

- **Engineering Prompts to Prevent Regression** — When adding new features, I learned to write prompts that explicitly preserve existing behavior (e.g., "don't include additional features beyond this"). This prevented scope creep and ensured each change was focused and testable.

- **Automated Testing with Pytest** — Writing tests alongside the code caught issues early. When the emoji theme update broke 7 tests, the test suite immediately revealed exactly what changed. Without those tests, the regression would have gone unnoticed until manual testing — if at all. Automated tests act as a safety net that lets you refactor with confidence.

## Built With

- Python 3.11
- Pytest
