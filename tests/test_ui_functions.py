import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# Mock pygame to avoid needing a display for testing
import pygame
import pygame.locals
import unittest.mock as mock

with mock.patch('pygame.display.set_mode'), \
     mock.patch('pygame.display.set_caption'), \
     mock.patch('pygame.font.SysFont'):
    
    # Import main after mocking pygame
    import main

class TestUIFunctions:
    def setup_method(self):
        """Set up for UI function tests."""
        # Reset the game instance
        main.game.reset_game()
    
    def test_reset_game_function(self):
        """Test the reset_game function."""
        # Modify the game state
        main.game.board[0][0] = "X"
        main.game.player = "O"
        main.game.game_over = True
        main.game.winner = "X"
        
        # Call the reset function
        main.reset_game()
        
        # Check that the game is reset to initial state
        assert all(cell is None for row in main.game.board for cell in row)
        assert main.game.player == "X"
        assert main.game.game_over == False
        assert main.game.winner is None
