## The Structure of the gameplay loop will exist in this file.

import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

# I prefer Sheldon Cooper's version of the game

RULES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}


def get_computer_choice():
    return random.choice(CHOICES)


def decide_winner(player, computer):
    # return "win", "loss", or "tie"
    pass
