## The Structure of the gameplay loop will exist in this file.

import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

# I prefer Sheldon Cooper's version of the game

RULES = {
    "rock": {"scissors": "crushes", "lizard": "crushes"},
    "paper": {"rock": "covers", "spock": "disproves"},
    "scissors": {"paper": "cuts", "lizard": "decapitates"},
    "lizard": {"spock": "poisons", "paper": "eats"},
    "spock": {"scissors": "smashes", "rock": "vaporizes"},
}


def get_computer_choice():
    return random.choice(CHOICES)


def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if computer in RULES[player]:
        return "win"
    return "loss"


# Computer's choice is checked against the two values held in each choice the player could select.
# If the computer's choice matches one of the values in the dictionary for the player's choice, a win is granted.

# Defaults to loss if neither of the conditions above it are met.
