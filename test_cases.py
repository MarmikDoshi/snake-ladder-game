import unittest

from dice_roll import DiceMovement


class TestGame(unittest.TestCase):

    def test_dice_type(self):
        """Test to check if the dice value is valid or not."""
        dice_movement = DiceMovement()
        dice_value = dice_movement.dice_roll('CROOKED')
        self.assertIn(dice_value, [2, 4, 6])


if __name__ == '__main__':
    unittest.main()
