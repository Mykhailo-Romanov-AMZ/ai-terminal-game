"""
A simple text-based game on a 5x5 grid.
Player starts at position (0, 0) — top-left corner.
"""

# Grid dimensions
GRID_SIZE = 5


def create_grid(size: int) -> list[list[str]]:
    """Create an empty grid filled with dots."""
    grid: list[list[str]] = []
    for row in range(size):
        grid.append(["."] * size)
    return grid


def place_player(grid: list[list[str]], row: int, col: int) -> None:
    """Place the player marker on the grid at the given position."""
    grid[row][col] = "P"


def draw_grid(grid: list[list[str]]) -> None:
    """Draw the grid to the terminal."""
    for row in grid:
        print(" ".join(row))


def game_loop() -> None:
    """Main game loop."""
    player_row = 0
    player_col = 0

    while True:
        # Build and draw the grid
        grid = create_grid(GRID_SIZE)
        place_player(grid, player_row, player_col)
        draw_grid(grid)

        # Wait for user input
        user_input = input("Enter 'q' to quit: ")

        if user_input == "q":
            print("Goodbye!")
            break


if __name__ == "__main__":
    game_loop()
