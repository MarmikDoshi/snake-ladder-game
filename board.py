import os
import sys

import pygame

from constants import BLACK, COLS, GREEN, HEIGHT, RED, ROWS, SQUARE_SIZE, WIDTH, WHITE
from dice_roll import DiceMovement


class Board:

    def __init__(self, dice_type):
        self.dice_type = dice_type

    def create_board(self):
        """Display board with snake."""

        win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('SNAKE AND LADDER GAME')
        win.fill(WHITE)

        dicemovement = DiceMovement()
        win.blit(pygame.image.load(os.path.join(sys.path[0]) + "/graphics/dice1.png"), (0, 650))
        pygame.display.update()

        run = True
        while run:
            self.draw_squares(win)
            self.add_snake(win)
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 125 and 650 <= mouse[1] <= 775:
                        dicemovement.add_dice(dicemovement, win, dicemovement.dice_roll(self.dice_type))

        pygame.quit()

    def draw_squares(self, win):
        """Add squares on the board with numbers."""
        colors = [
            # for even number row
            [RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN],
            # for odd number row
            [GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED]
        ]
        top = SQUARE_SIZE*10
        for row in range(1, ROWS + 1):
            top -= SQUARE_SIZE
            is_even_row = (row-1) % 2
            left = 0
            for col in range(1, COLS + 1):
                box = colors[(row-1) % 2][col-1]
                left += SQUARE_SIZE
                pygame.draw.rect(win, box, (left, top, SQUARE_SIZE, SQUARE_SIZE))

                small_font = pygame.font.SysFont('Corbel', 15)
                text = small_font.render(str((row-1) * 10 + 11 - col if is_even_row else (row-1)*10 + col), True, BLACK)
                win.blit(text, (left, top))

    def add_snake(self, win):
        """Add snake on the board."""
        win.blit(pygame.image.load((os.path.join(sys.path[0]) + "/graphics/snake.png")), (140, 275))

    def add_piece(self, win):
        """Add player on the board."""
        win.blit(pygame.image.load((os.path.join(sys.path[0]) + "/graphics/redpiece.png")),
                 (10, 550))

