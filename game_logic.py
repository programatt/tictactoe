class TicTacToeGame:
    def __init__(self):
        self.BOARD_SIZE = 3
        self.board = [[None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.player = "X"
        self.game_over = False
        self.winner = None

    def mark_square(self, row, col, player):
        """Mark a square on the board if it's empty."""
        if self.board[row][col] is None:
            self.board[row][col] = player
            return True
        return False

    def check_win(self, player):
        """Check if the given player has won."""
        # Check rows
        for row in range(self.BOARD_SIZE):
            if all(self.board[row][col] == player for col in range(self.BOARD_SIZE)):
                return True
        
        # Check columns
        for col in range(self.BOARD_SIZE):
            if all(self.board[row][col] == player for row in range(self.BOARD_SIZE)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(self.BOARD_SIZE)):
            return True
        
        if all(self.board[i][self.BOARD_SIZE - 1 - i] == player for i in range(self.BOARD_SIZE)):
            return True
        
        return False

    def check_tie(self):
        """Check if the game is tied (board is full)."""
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if self.board[row][col] is None:
                    return False
        return True

    def switch_player(self):
        """Switch the current player."""
        self.player = "O" if self.player == "X" else "X"

    def reset_game(self):
        """Reset the game to initial state."""
        self.board = [[None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        """Make a move for the current player."""
        if self.game_over:
            return False
            
        if self.mark_square(row, col, self.player):
            if self.check_win(self.player):
                self.game_over = True
                self.winner = self.player
            elif self.check_tie():
                self.game_over = True
            else:
                self.switch_player()
            return True
        return False
