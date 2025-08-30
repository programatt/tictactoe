import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
size = 256, 256
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe Icon")

# Colors
BG_COLOR = (28, 170, 156)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
LINE_WIDTH = 8
CIRCLE_WIDTH = 8
CROSS_WIDTH = 8

# Fill the background
screen.fill(BG_COLOR)

# Draw a simplified Tic Tac Toe grid
pygame.draw.line(screen, (23, 145, 135), (85, 20), (85, 236), LINE_WIDTH)
pygame.draw.line(screen, (23, 145, 135), (171, 20), (171, 236), LINE_WIDTH)
pygame.draw.line(screen, (23, 145, 135), (20, 85), (236, 85), LINE_WIDTH)
pygame.draw.line(screen, (23, 145, 135), (20, 171), (236, 171), LINE_WIDTH)

# Draw an X in the center
pygame.draw.line(screen, CROSS_COLOR, (95, 95), (161, 161), CROSS_WIDTH)
pygame.draw.line(screen, CROSS_COLOR, (161, 95), (95, 161), CROSS_WIDTH)

# Draw a circle in the top left
pygame.draw.circle(screen, CIRCLE_COLOR, (42, 42), 25, CIRCLE_WIDTH)

# Draw a circle in the bottom right
pygame.draw.circle(screen, CIRCLE_COLOR, (214, 214), 25, CIRCLE_WIDTH)

# Update the display
pygame.display.flip()

# Save the icon
pygame.image.save(screen, "tictactoe-icon.png")

# Quit
pygame.quit()
sys.exit()
