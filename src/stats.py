## The game's primary save functions exist in this file.
import json
from pathlib import Path

STATS_FILE = Path(__file__).parent / "stats.json"
DEFAULT_STATS = {"wins": 0, "losses": 0, "ties": 0}


def load_stats():
    try:
        with open(STATS_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_STATS.copy()
    return {key: data.get(key, 0) for key in DEFAULT_STATS}


# Try/Else allows the program to run when the stats file does not exist yet.


def save_stats():
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


# Stats are written into Json file

stats = load_stats()


def record_result(result):
    if result == "win":
        stats["wins"] += 1
    elif result == "loss":
        stats["losses"] += 1
    elif result == "tie":
        stats["ties"] += 1
    save_stats()


def show_stats():
    print("\n=== Overall Stats ===")
    print(f"Wins:   {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Ties:   {stats['ties']}")


# This function is used to display the overall stats that have been accumulated across every run of this program.
