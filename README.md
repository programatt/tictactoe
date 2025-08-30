# Tic Tac Toe Game for Ubuntu

A simple 2-player Tic Tac Toe game built with Pygame, packaged as a .deb installer for Ubuntu 24.04.

## Installation

To install the game on Ubuntu 24.04, use the following command:

```bash
sudo dpkg -i tictactoe_1.0_amd64.deb
```

The package will automatically install python3-pygame if it's not already installed on your system.

## Usage

After installation, you can launch the game in two ways:

1. From the terminal:
   ```bash
   tictactoe
   ```

2. From the applications menu:
   - Open the Applications menu
   - Navigate to the Games section
   - Click on "Tic Tac Toe"

## Game Instructions

- Player X always goes first
- Players take turns clicking on the grid to place their marks
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins
- If all squares are filled with no winner, the game is a tie
- Press 'R' to restart the game at any time

## Uninstallation

To uninstall the game, use:

```bash
sudo apt remove tictactoe
