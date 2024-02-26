"""Argument: is a legendary game for settling disputes"""


import random


def read_ratings(filename: str, user_name: str) -> int:
    """Read ratings from the given file and return the rating for the specified user."""
    user_rating = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, rating = line.strip().split()
                if name == user_name:
                    user_rating = int(rating)
                    break
    except FileNotFoundError:
        pass
    return user_rating


def update_ratings(filename: str, user_name: str, user_score: int):
    """Update ratings file with the new score for the user."""
    ratings = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, rating = line.strip().split()
                ratings[name] = rating
    except FileNotFoundError:
        pass
    ratings[user_name] = str(user_score)

    with open(filename, 'w') as file:
        for name, rating in ratings.items():
            file.write(f"{name} {rating}\n")


def determine_winner(user_choice: str, computer_choice: str, options: list[str]) -> tuple[str, str]:
    """Determine the winner between user and computer based on choices."""
    if user_choice == computer_choice:
        return "Draw", computer_choice

    user_index = options.index(user_choice)
    computer_index = options.index(computer_choice)
    options_count = len(options)
    half_options_count = options_count // 2

    if (user_index - computer_index) % options_count in range(1, half_options_count + 1):
        return "Win", computer_choice
    else:
        return "Lose", computer_choice


def main():
    """Main function to run the game."""
    print("Enter your name:", end=" ")
    user_name = input()
    print("Hello,", user_name)

    print("Enter options (separated by commas) or leave empty for default (rock, paper, scissors):", end=" ")
    options_input = input().strip()
    if options_input:
        options = [option.strip() for option in options_input.split(",")]
    else:
        options = ["rock", "paper", "scissors"]


    print("Okay, let's start.")

    user_score = 0

    while True:
        print("> ", end="")
        user_choice = input().strip()

        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print("Your rating:", user_score)
        elif user_choice in options:
            computer_choice = random.choice(options)
            result, computer_choice = determine_winner(user_choice, computer_choice, options)
            if result == "Draw":
                user_score += 50
                print(f"There is a draw ({computer_choice})")
            elif result == "Win":
                user_score += 100
                print(f"Well done. The computer chose {computer_choice} and failed")
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
