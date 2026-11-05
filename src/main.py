## Main File for game

from game import CHOICES, get_computer_choice, decide_winner
from stats import record_result, show_stats


def show_menu(): ...


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
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a tie!")

        record_result(result)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Returning to the main menu...")
            break


def main(): ...


if __name__ == "__main__":
    main()
