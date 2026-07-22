"""
Tests for game.py — verifies grid creation, player placement, movement, collectibles, and hazards.
"""

from game import (
    create_grid, place_player, place_collectible, spawn_collectible,
    place_hazard, spawn_hazard, handle_move, GRID_SIZE,
    PLAYER_EMOJI, COLLECTIBLE_EMOJI, HAZARD_EMOJI, EMPTY_EMOJI
)


def test_grid_is_5x5():
    """The grid should have 5 rows and 5 columns."""
    grid = create_grid(GRID_SIZE)
    # Check we have 5 rows
    assert len(grid) == 5
    # Check each row has 5 columns
    for row in grid:
        assert len(row) == 5


def test_grid_is_filled_with_dots():
    """Every cell in a fresh grid should be empty."""
    grid = create_grid(GRID_SIZE)
    for row in grid:
        for cell in row:
            assert cell == EMPTY_EMOJI


def test_player_starts_at_origin():
    """Player should start at position (0, 0)."""
    grid = create_grid(GRID_SIZE)
    player_row = 0
    player_col = 0
    place_player(grid, player_row, player_col)
    # The top-left cell should be the player emoji
    assert grid[0][0] == PLAYER_EMOJI


def test_player_only_occupies_one_cell():
    """Only one cell should be the player, the rest should be empty."""
    grid = create_grid(GRID_SIZE)
    place_player(grid, 0, 0)
    # Count how many cells contain the player emoji
    p_count = 0
    for row in grid:
        for cell in row:
            if cell == PLAYER_EMOJI:
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


# --- Collectible tests ---


def test_place_collectible_on_grid():
    """The collectible should appear on the grid."""
    grid = create_grid(GRID_SIZE)
    place_collectible(grid, 2, 3)
    assert grid[2][3] == COLLECTIBLE_EMOJI


def test_spawn_collectible_not_on_player():
    """The collectible should never spawn on the player's position."""
    for _ in range(50):
        row, col = spawn_collectible(2, 2, GRID_SIZE)
        assert (row, col) != (2, 2)


def test_spawn_collectible_within_grid():
    """The collectible should always be within grid bounds."""
    for _ in range(50):
        row, col = spawn_collectible(0, 0, GRID_SIZE)
        assert 0 <= row < GRID_SIZE
        assert 0 <= col < GRID_SIZE


# --- Hazard tests ---


def test_place_hazard_on_grid():
    """The hazard should appear on the grid."""
    grid = create_grid(GRID_SIZE)
    place_hazard(grid, 3, 4)
    assert grid[3][4] == HAZARD_EMOJI


def test_place_hazard_only_occupies_one_cell():
    """Only one cell should be the hazard when placed."""
    grid = create_grid(GRID_SIZE)
    place_hazard(grid, 2, 2)
    x_count = 0
    for row in grid:
        for cell in row:
            if cell == HAZARD_EMOJI:
                x_count += 1
    assert x_count == 1


def test_spawn_hazard_not_on_player():
    """The hazard should never spawn on the player's position."""
    for _ in range(50):
        row, col = spawn_hazard(2, 2, 4, 4, GRID_SIZE)
        assert (row, col) != (2, 2)


def test_spawn_hazard_not_on_collectible():
    """The hazard should never spawn on the collectible's position."""
    for _ in range(50):
        row, col = spawn_hazard(0, 0, 3, 3, GRID_SIZE)
        assert (row, col) != (3, 3)


def test_spawn_hazard_within_grid():
    """The hazard should always spawn within grid bounds."""
    for _ in range(50):
        row, col = spawn_hazard(0, 0, 1, 1, GRID_SIZE)
        assert 0 <= row < GRID_SIZE
        assert 0 <= col < GRID_SIZE


def test_hazard_does_not_overwrite_player():
    """Placing the hazard should not overwrite the player on the grid."""
    grid = create_grid(GRID_SIZE)
    place_player(grid, 1, 1)
    place_hazard(grid, 3, 3)
    assert grid[1][1] == PLAYER_EMOJI
    assert grid[3][3] == HAZARD_EMOJI
