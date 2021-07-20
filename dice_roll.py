import random
import os
import sys

import pygame

import constants


class DiceMovement:
    """Dice throw and player movements."""

    def __init__(self, ):
        self.player_position = 0

    def add_dice(self, dice_movement, win, dice_number):
        """Add dice in the game and move the player position accordingly."""
        win.blit(pygame.image.load(os.path.join(sys.path[0]) + "/graphics/dice" + str(dice_number) + ".png"), (0, 650))
        dice_movement.move_player(win, dice_number)

    def dice_roll(self, dice_type):
        """Return the random value for dice roll."""
        dice_value = 0
        if dice_type == 'NORMAL':
            dice_value = random.randint(1, 6)
        elif dice_type == 'CROOKED':
            dice_value = random.randrange(2, 8, 2)
        return dice_value

    def move_player(self, win, dice_output):
        """Initialize the game for the player starting position at 0."""
        self.player_position += dice_output

        if self.player_position in constants.SNAKE:
            self.player_position = constants.SNAKE[dice_output]

        win.blit(pygame.image.load(os.path.join(sys.path[0]) + "/graphics/redpiece.png"), (10 + dice_output, 550))
        pygame.display.update()
