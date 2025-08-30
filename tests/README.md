# Tic Tac Toe Test Suite

This directory contains the test suite for the Tic Tac Toe game.

## Test Structure

- `test_game_logic.py`: Tests for the core game logic in `game_logic.py`
- `test_ui_functions.py`: Tests for UI functions in `main.py` (using mocks for pygame)

## Running Tests

To run all tests:

```bash
python -m pytest tests/
```

To run tests with coverage report:

```bash
python -m pytest tests/ --cov
```

## Coverage

The test suite achieves 100% coverage for the core game logic in `game_logic.py`. The overall project coverage is lower due to pygame UI code in `main.py` that is difficult to test without a display.

## Test Organization

Tests are organized by the components they test:

1. **Game State Management**: Tests for initializing and resetting the game state
2. **Move Validation**: Tests for marking squares and handling invalid moves
3. **Win Detection**: Tests for detecting wins in rows, columns, and diagonals
4. **Tie Detection**: Tests for detecting tie games
5. **Player Management**: Tests for switching players
6. **Game Flow**: Tests for the complete game flow including wins and ties
