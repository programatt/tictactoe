import pytest
from game_logic import TicTacToeGame

class TestTicTacToeGame:
    def setup_method(self):
        """Set up a new game instance before each test."""
        self.game = TicTacToeGame()
    
    def test_initial_state(self):
        """Test that the game initializes with the correct default state."""
        assert self.game.BOARD_SIZE == 3
        assert len(self.game.board) == 3
        assert all(len(row) == 3 for row in self.game.board)
        assert all(cell is None for row in self.game.board for cell in row)
        assert self.game.player == "X"
        assert self.game.game_over == False
        assert self.game.winner is None
    
    def test_mark_square_valid(self):
        """Test marking a square with a valid player."""
        result = self.game.mark_square(0, 0, "X")
        assert result == True
        assert self.game.board[0][0] == "X"
    
    def test_mark_square_invalid(self):
        """Test marking a square that is already occupied."""
        self.game.mark_square(0, 0, "X")
        result = self.game.mark_square(0, 0, "O")
        assert result == False
        assert self.game.board[0][0] == "X"
    
    def test_check_win_rows(self):
        """Test checking for a win in rows."""
        # Set up a winning row
        self.game.board[0] = ["X", "X", "X"]
        assert self.game.check_win("X") == True
        assert self.game.check_win("O") == False
    
    def test_check_win_columns(self):
        """Test checking for a win in columns."""
        # Set up a winning column
        self.game.board[0][0] = "O"
        self.game.board[1][0] = "O"
        self.game.board[2][0] = "O"
        assert self.game.check_win("O") == True
        assert self.game.check_win("X") == False
    
    def test_check_win_diagonal_main(self):
        """Test checking for a win in the main diagonal."""
        # Set up a winning main diagonal
        self.game.board[0][0] = "X"
        self.game.board[1][1] = "X"
        self.game.board[2][2] = "X"
        assert self.game.check_win("X") == True
        assert self.game.check_win("O") == False
    
    def test_check_win_diagonal_anti(self):
        """Test checking for a win in the anti-diagonal."""
        # Set up a winning anti-diagonal
        self.game.board[0][2] = "O"
        self.game.board[1][1] = "O"
        self.game.board[2][0] = "O"
        assert self.game.check_win("O") == True
        assert self.game.check_win("X") == False
    
    def test_check_win_no_win(self):
        """Test checking for a win when there is no winner."""
        # Set up a board with no winner
        self.game.board[0][0] = "X"
        self.game.board[0][1] = "O"
        self.game.board[0][2] = "X"
        self.game.board[1][0] = "O"
        self.game.board[1][1] = "X"
        self.game.board[1][2] = "O"
        assert self.game.check_win("X") == False
        assert self.game.check_win("O") == False
    
    def test_check_tie_full_board(self):
        """Test checking for a tie with a full board."""
        # Set up a full board with no winner
        self.game.board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        assert self.game.check_tie() == True
    
    def test_check_tie_partial_board(self):
        """Test checking for a tie with a partial board."""
        # Set up a partial board
        self.game.board[0][0] = "X"
        self.game.board[0][1] = "O"
        assert self.game.check_tie() == False
    
    def test_switch_player(self):
        """Test switching the current player."""
        assert self.game.player == "X"
        self.game.switch_player()
        assert self.game.player == "O"
        self.game.switch_player()
        assert self.game.player == "X"
    
    def test_reset_game(self):
        """Test resetting the game to initial state."""
        # Modify the game state
        self.game.board[0][0] = "X"
        self.game.player = "O"
        self.game.game_over = True
        self.game.winner = "X"
        
        # Reset the game
        self.game.reset_game()
        
        # Check that the game is reset to initial state
        assert all(cell is None for row in self.game.board for cell in row)
        assert self.game.player == "X"
        assert self.game.game_over == False
        assert self.game.winner is None
    
    def test_make_move_valid(self):
        """Test making a valid move."""
        result = self.game.make_move(0, 0)
        assert result == True
        assert self.game.board[0][0] == "X"
    
    def test_make_move_invalid(self):
        """Test making a move in an occupied square."""
        self.game.make_move(0, 0)  # First move by X
        result = self.game.make_move(0, 0)  # Try to move in the same square
        assert result == False
        assert self.game.board[0][0] == "X"
    
    def test_make_move_win(self):
        """Test making a move that results in a win."""
        # Set up a board where X can win with one more move
        self.game.board = [
            ["X", "X", None],
            [None, None, None],
            [None, None, None]
        ]
        self.game.player = "X"
        
        # Make the winning move
        result = self.game.make_move(0, 2)
        assert result == True
        assert self.game.game_over == True
        assert self.game.winner == "X"
    
    def test_make_move_tie(self):
        """Test making a move that results in a tie."""
        # Set up a board where the next move will result in a tie
        self.game.board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", None, "X"]
        ]
        self.game.player = "O"
        
        # Make the move that results in a tie
        result = self.game.make_move(2, 1)
        assert result == True
        assert self.game.game_over == True
        assert self.game.winner is None
    
    def test_make_move_after_game_over(self):
        """Test making a move after the game is over."""
        # Set up a win condition
        self.game.board = [
            ["X", "X", None],
            [None, None, None],
            [None, None, None]
        ]
        self.game.player = "X"
        
        # Make the winning move
        self.game.make_move(0, 2)
        
        # Try to make another move after game over
        result = self.game.make_move(1, 1)
        assert result == False
        assert self.game.board[1][1] is None
