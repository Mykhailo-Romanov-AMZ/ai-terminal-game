"""
Tests for game.py — verifies grid creation and player placement.
"""

from game import create_grid, place_player, GRID_SIZE


def test_grid_is_5x5():
    """The grid should have 5 rows and 5 columns."""
    grid = create_grid(GRID_SIZE)
    # Check we have 5 rows
    assert len(grid) == 5
    # Check each row has 5 columns
    for row in grid:
        assert len(row) == 5


def test_grid_is_filled_with_dots():
    """Every cell in a fresh grid should be a dot."""
    grid = create_grid(GRID_SIZE)
    for row in grid:
        for cell in row:
            assert cell == "."


def test_player_starts_at_origin():
    """Player should start at position (0, 0)."""
    grid = create_grid(GRID_SIZE)
    player_row = 0
    player_col = 0
    place_player(grid, player_row, player_col)
    # The top-left cell should be "P"
    assert grid[0][0] == "P"


def test_player_only_occupies_one_cell():
    """Only one cell should be the player, the rest should be dots."""
    grid = create_grid(GRID_SIZE)
    place_player(grid, 0, 0)
    # Count how many cells contain "P"
    p_count = 0
    for row in grid:
        for cell in row:
            if cell == "P":
                p_count += 1
    assert p_count == 1
