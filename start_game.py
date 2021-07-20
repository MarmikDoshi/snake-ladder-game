import pygame

from board import Board
from constants import CROOKED_DICE, GREEN, NORMAL_DICE, RED, WIDTH, HEIGHT, WHITE


class Game:
    """Initialize the game."""

    def __init__(self):
        self.dice_type = NORMAL_DICE
        self.main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.init()

    def play(self):
        """Start the game."""
        pygame.display.set_caption('SNAKE AND LADDER GAME')
        run = True

        while run:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH / 2 - 80 <= mouse[0] <= WIDTH / 2 + 80 and HEIGHT / 2 - 100 <= mouse[1] <= HEIGHT / 2 - 60:
                        self.dice_type = NORMAL_DICE
                        board = Board(self.dice_type)
                        board.create_board()

                    if WIDTH / 2 - 80 <= mouse[0] <= WIDTH / 2 + 80 and HEIGHT / 2 + 100 <= mouse[1] <= HEIGHT / 2 + 140:
                        self.dice_type = CROOKED_DICE
                        board = Board(self.dice_type)
                        board.create_board()

            self.main_screen.fill(WHITE)
            small_font = pygame.font.SysFont('Italic', 25)

            text = small_font.render('NORMAL DICE', True, RED)
            pygame.draw.rect(self.main_screen, GREEN, [WIDTH/2-80, HEIGHT/2-100, 160, 40])
            self.main_screen.blit(text, (WIDTH/2-80, HEIGHT/2-100))

            text = small_font.render('CROOKED DICE', True, RED)
            pygame.draw.rect(self.main_screen, GREEN, [WIDTH/2-80, HEIGHT/2+100, 160, 40])
            self.main_screen.blit(text, (WIDTH/2-80, HEIGHT/2+100))

            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.play()
