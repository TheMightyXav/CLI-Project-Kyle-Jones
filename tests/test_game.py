# tests/test_game.py
import unittest
from unittest.mock import patch

from src.game import CHOICES, RULES, get_computer_choice, decide_winner


class TestComputerChoice(unittest.TestCase):
    # Class is being used to create a blueprint for the tests present in this file and the answers that the computer picks. Claude explained the use cases of 'class' and it has been added to this test file.
    def test_choice_is_always_valid(self):
        for _ in range(1000):
            self.assertIn(get_computer_choice(), CHOICES)

    # self refers to the test instance in each of these functions, and passes the data from each instance through the function. Python assigns all values to self, rather than it being manually defined by me.
    def test_every_choice_can_appear(self):
        seen = {get_computer_choice() for _ in range(1000)}
        self.assertEqual(seen, set(CHOICES))

    # Computer is tested 1000 to make sure that each choice is included in its decision making
    def test_distribution_is_roughly_even(self):
        counts = {choice: 0 for choice in CHOICES}
        for _ in range(1000):
            counts[get_computer_choice()] += 1

        for choice, count in counts.items():
            self.assertTrue(100 <= count <= 300, f"{choice} appeared {count} times")

    def test_picks_from_the_choices_list(self):
        with patch("src.game.random.choice", return_value="rock") as mock_choice:
            result = get_computer_choice()

        mock_choice.assert_called_once_with(CHOICES)
        self.assertEqual(result, "rock")


class TestDecideWinner(unittest.TestCase):
    def test_ties(self):
        for choice in CHOICES:
            self.assertEqual(decide_winner(choice, choice), "tie")

    def test_wins_and_losses(self):
        for winner in CHOICES:
            for loser in RULES[winner]:
                self.assertEqual(decide_winner(winner, loser), "win")
                self.assertEqual(decide_winner(loser, winner), "loss")


if __name__ == "__main__":
    unittest.main()
