"""
Tests for game.py — verifies grid creation, player placement, and movement.
"""

from game import create_grid, place_player, handle_move, GRID_SIZE


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


# --- Movement tests ---


def test_move_w_goes_up():
    """W should decrease the row by 1."""
    row, col = handle_move("w", 2, 2, GRID_SIZE)
    assert row == 1
    assert col == 2


def test_move_s_goes_down():
    """S should increase the row by 1."""
    row, col = handle_move("s", 2, 2, GRID_SIZE)
    assert row == 3
    assert col == 2


def test_move_a_goes_left():
    """A should decrease the column by 1."""
    row, col = handle_move("a", 2, 2, GRID_SIZE)
    assert row == 2
    assert col == 1


def test_move_d_goes_right():
    """D should increase the column by 1."""
    row, col = handle_move("d", 2, 2, GRID_SIZE)
    assert row == 2
    assert col == 3


def test_cannot_move_above_top():
    """Moving up from row 0 should stay at row 0."""
    row, col = handle_move("w", 0, 2, GRID_SIZE)
    assert row == 0
    assert col == 2


def test_cannot_move_below_bottom():
    """Moving down from the bottom row should stay put."""
    row, col = handle_move("s", GRID_SIZE - 1, 2, GRID_SIZE)
    assert row == GRID_SIZE - 1
    assert col == 2


def test_cannot_move_left_of_grid():
    """Moving left from column 0 should stay at column 0."""
    row, col = handle_move("a", 2, 0, GRID_SIZE)
    assert row == 2
    assert col == 0


def test_cannot_move_right_of_grid():
    """Moving right from the last column should stay put."""
    row, col = handle_move("d", 2, GRID_SIZE - 1, GRID_SIZE)
    assert row == 2
    assert col == GRID_SIZE - 1
