"""
A simple text-based game on a 5x5 grid.
Player starts at position (0, 0) — top-left corner.
Use WASD to move: W=up, A=left, S=down, D=right.
Collect the item (*) to score points. Reach 10 to win!
"""

import os
import random

# Grid dimensions
GRID_SIZE = 5

# Win condition
WIN_SCORE = 10


def create_grid(size: int) -> list[list[str]]:
    """Create an empty grid filled with dots."""
    grid: list[list[str]] = []
    for row in range(size):
        grid.append(["."] * size)
    return grid


def place_player(grid: list[list[str]], row: int, col: int) -> None:
    """Place the player marker on the grid at the given position."""
    grid[row][col] = "P"


def place_collectible(grid: list[list[str]], row: int, col: int) -> None:
    """Place the collectible marker on the grid."""
    grid[row][col] = "*"


def spawn_collectible(player_row: int, player_col: int, grid_size: int) -> tuple[int, int]:
    """Return a random position for the collectible that is not on the player."""
    while True:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if row != player_row or col != player_col:
            return row, col


def draw_grid(grid: list[list[str]]) -> None:
    """Draw the grid to the terminal."""
    for row in grid:
        print(" ".join(row))


def handle_move(direction: str, player_row: int, player_col: int, grid_size: int) -> tuple[int, int]:
    """Return the new position after moving in the given direction.
    If the move would go outside the grid, stay put."""
    new_row = player_row
    new_col = player_col

    if direction == "w":
        new_row = player_row - 1
    elif direction == "s":
        new_row = player_row + 1
    elif direction == "a":
        new_col = player_col - 1
    elif direction == "d":
        new_col = player_col + 1

    # Boundary check — only move if still inside the grid
    if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
        return new_row, new_col
    else:
        return player_row, player_col


def game_loop() -> None:
    """Main game loop."""
    player_row = 0
    player_col = 0
    score = 0

    # Spawn the first collectible
    collectible_row, collectible_col = spawn_collectible(player_row, player_col, GRID_SIZE)

    while True:
        # Clear the terminal
        os.system("clear")

        # Display score
        print(f"Score: {score}/{WIN_SCORE}")
        print()

        # Build and draw the grid
        grid = create_grid(GRID_SIZE)
        place_collectible(grid, collectible_row, collectible_col)
        place_player(grid, player_row, player_col)
        draw_grid(grid)

        # Wait for user input
        user_input = input("\nMove (WASD) or 'q' to quit: ")

        if user_input == "q":
            print("Goodbye!")
            break

        # Handle movement
        if user_input in ("w", "a", "s", "d"):
            player_row, player_col = handle_move(user_input, player_row, player_col, GRID_SIZE)

            # Check if player collected the item
            if player_row == collectible_row and player_col == collectible_col:
                score += 1

                # Check win condition
                if score >= WIN_SCORE:
                    os.system("clear")
                    print(f"Score: {score}/{WIN_SCORE}")
                    print()
                    grid = create_grid(GRID_SIZE)
                    place_player(grid, player_row, player_col)
                    draw_grid(grid)
                    print("\nYou win! Congratulations!")
                    break

                # Respawn collectible
                collectible_row, collectible_col = spawn_collectible(player_row, player_col, GRID_SIZE)


if __name__ == "__main__":
    game_loop()
