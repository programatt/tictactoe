import pygame
import sys
from game_logic import TicTacToeGame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 700
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE
LINE_WIDTH = 15
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
CIRCLE_RADIUS = CELL_SIZE // 3
SPACE = CELL_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game instance
game = TicTacToeGame()

# Font
font = pygame.font.SysFont(None, 40)

def draw_board():
    # Draw background
    screen.fill(BG_COLOR)
    
    # Draw horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)
    
    # Draw vertical lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT - 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT - 100), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if game.board[row][col] == "O":
                # Draw circle
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH
                )
            elif game.board[row][col] == "X":
                # Draw cross
                # Descending line
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE),
                    CROSS_WIDTH
                )
                # Ascending line
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    CROSS_WIDTH
                )

def draw_status():
    # Draw status area
    pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT - 100, WIDTH, 100))
    
    if game.game_over:
        if game.winner:
            text = font.render(f"Player {game.winner} wins! Press R to restart", True, TEXT_COLOR)
        else:
            text = font.render("Game Tied! Press R to restart", True, TEXT_COLOR)
    else:
        text = font.render(f"Player {game.player}'s turn", True, TEXT_COLOR)
    
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50 - text.get_height() // 2))

def reset_game():
    game.reset_game()

def main():
    # Draw initial board
    draw_board()
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                
                # Check if click is within board
                if mouseY < HEIGHT - 100:
                    clicked_row = mouseY // CELL_SIZE
                    clicked_col = mouseX // CELL_SIZE
                    
                    game.make_move(clicked_row, clicked_col)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
        
        # Draw everything
        draw_board()
        draw_figures()
        draw_status()
        
        # Update the display
        pygame.display.update()

if __name__ == "__main__":
    main()
