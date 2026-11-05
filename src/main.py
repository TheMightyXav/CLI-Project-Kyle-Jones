## Main File for game

from game import CHOICES, get_computer_choice, decide_winner, describe_win
from stats import record_result, show_stats


def show_menu():
    print("\n=== Rock, Paper, Scissors, Lizard, Spock ===")
    print("1) Play new game")
    print("2) View Overall Stats")
    print("3) Exit")


# Validation step
def get_player_choice():
    while True:
        print("\nChoices: " + ", ".join(CHOICES))
        choice = input("Enter your choice: ").strip().lower()

        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type one of the options exactly.")


def play_game():
    while True:
        player = get_player_choice()
        computer = get_computer_choice()

        print(f"\nYou chose {player}.")
        print(f"The computer chose {computer}.")

        result = decide_winner(player, computer)

        if result == "win":
            print(f"{describe_win(player, computer)}. You win!")
        elif result == "loss":
            print(f"{describe_win(computer, player)}. You lose!")
        else:
            print(f"Both chose {player}. It's a tie!")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Returning to the main menu...")
            break


# This is the base gameplay loop.
# The message printed after the player chooses an option describes how that option interacts with the one chosen by the computer.


def main(): ...


if __name__ == "__main__":
    main()
