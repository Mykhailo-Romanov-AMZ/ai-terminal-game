"""
Score with Messi
A text-based game on a 5x5 grid.
Messi tries to score all the goals in universe.
Use WASD to move: W=up, A=left, S=down, D=right.
Collect footballs to score. Avoid Lamine Yamal!
"""

import os
import random

# Game info
GAME_NAME = "Score with Messi"
STORY_INTRO = "Messi tries to score all the goals in universe"

# Grid dimensions
GRID_SIZE = 5

# Win condition
WIN_SCORE = 10

# Emojis
PLAYER_EMOJI = "⭐"
COLLECTIBLE_EMOJI = "⚽"
HAZARD_EMOJI = "💀"
EMPTY_EMOJI = "·"

# Messages
WIN_MESSAGE = "Yes, Messi the Champion!"
LOSE_MESSAGE = "Youth Wins... for now"


def show_intro() -> None:
    """Display the game name and story intro."""
    os.system("clear")
    print("=" * 40)
    print(f"  {GAME_NAME}")
    print("=" * 40)
    print()
    print(f"  {STORY_INTRO}")
    print()
    print(f"  Use WASD to move.")
    print(f"  Collect {COLLECTIBLE_EMOJI} to score {WIN_SCORE} goals.")
    print(f"  Avoid {HAZARD_EMOJI}!")
    print()
    print("=" * 40)
    input("  Press Enter to start...")


def create_grid(size: int) -> list[list[str]]:
    """Create an empty grid filled with dots."""
    grid: list[list[str]] = []
    for row in range(size):
        grid.append([EMPTY_EMOJI] * size)
    return grid


def place_player(grid: list[list[str]], row: int, col: int) -> None:
    """Place the player marker on the grid at the given position."""
    grid[row][col] = PLAYER_EMOJI


def place_collectible(grid: list[list[str]], row: int, col: int) -> None:
    """Place the collectible marker on the grid."""
    grid[row][col] = COLLECTIBLE_EMOJI


def spawn_collectible(player_row: int, player_col: int, grid_size: int) -> tuple[int, int]:
    """Return a random position for the collectible that is not on the player."""
    while True:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if row != player_row or col != player_col:
            return row, col


def place_hazard(grid: list[list[str]], row: int, col: int) -> None:
    """Place the hazard marker on the grid."""
    grid[row][col] = HAZARD_EMOJI


def spawn_hazard(player_row: int, player_col: int, collectible_row: int, collectible_col: int, grid_size: int) -> tuple[int, int]:
    """Return a random position for the hazard that is not on the player or collectible."""
    while True:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if (row, col) != (player_row, player_col) and (row, col) != (collectible_row, collectible_col):
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
    show_intro()

    playing = True

    while playing:
        # Reset game state for a new game
        player_row = 0
        player_col = 0
        score = 0

        # Spawn the first collectible
        collectible_row, collectible_col = spawn_collectible(player_row, player_col, GRID_SIZE)

        # Spawn the hazard
        hazard_row, hazard_col = spawn_hazard(player_row, player_col, collectible_row, collectible_col, GRID_SIZE)

        game_active = True

        while game_active:
            # Clear the terminal
            os.system("clear")

            # Display score
            print(f"{GAME_NAME}")
            print(f"Score: {score}/{WIN_SCORE}")
            print()

            # Build and draw the grid
            grid = create_grid(GRID_SIZE)
            place_collectible(grid, collectible_row, collectible_col)
            place_hazard(grid, hazard_row, hazard_col)
            place_player(grid, player_row, player_col)
            draw_grid(grid)

            # Wait for user input
            user_input = input("\nMove (WASD) or 'q' to quit: ")

            if user_input == "q":
                print("Goodbye!")
                return

            # Handle movement
            if user_input in ("w", "a", "s", "d"):
                player_row, player_col = handle_move(user_input, player_row, player_col, GRID_SIZE)

                # Check if player hit the hazard
                if player_row == hazard_row and player_col == hazard_col:
                    os.system("clear")
                    print(f"Score: {score}/{WIN_SCORE}")
                    print()
                    print(LOSE_MESSAGE)
                    game_active = False

                # Check if player collected the item
                elif player_row == collectible_row and player_col == collectible_col:
                    score += 1

                    # Check win condition
                    if score >= WIN_SCORE:
                        os.system("clear")
                        print(f"Score: {score}/{WIN_SCORE}")
                        print()
                        grid = create_grid(GRID_SIZE)
                        place_player(grid, player_row, player_col)
                        draw_grid(grid)
                        print(f"\n{WIN_MESSAGE}")
                        game_active = False
                    else:
                        # Respawn collectible
                        collectible_row, collectible_col = spawn_collectible(player_row, player_col, GRID_SIZE)

        # Ask to play again
        play_again = input("\nPlay again? (y/n): ")
        if play_again != "y":
            playing = False


if __name__ == "__main__":
    game_loop()
