"""Newton: arithmetic testing program"""

import random


def generate_question(level: int) -> tuple[str, int]:
    """
    Generates an arithmetic question depending on the complexity level.

    Args:
        level (int): The complexity level (1 or 2).

    Returns:
        tuple[str, int]: A tuple containing the question and the correct answer.
    """
    question = ""
    correct_answer = ""
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        question = f"{num1} {operation} {num2}"
        correct_answer = eval(question)
    elif level == 2:
        num = random.randint(11, 29)
        question = f"{num}"
        correct_answer = num ** 2
    return question, correct_answer


def ask_question() -> int:
    """
    Asks the user for an answer and validates it.

    Returns:
        int: The user's input.
    """
    try:
        answer = int(input("> "))
    except ValueError:
        print("Incorrect format.")
        return ask_question()
    return answer


def main() -> None:
    """
    The main function of the program. Controls the test execution.
    """
    print("Which level do you want? Enter a number:\n"
          " 1 - simple operations with numbers 2-9\n"
          " 2 - integral squares of 11-29")
    while True:
        try:
            level = int(input("> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    correct_answers = 0
    for _ in range(5):
        question, correct_answer = generate_question(level)
        print(question)
        user_answer = ask_question()
        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save_result = input("> ").lower()
    if save_result in ['yes', 'y']:
        print("What is your name?")
        name = input("> ")
        with open("results.txt", "a") as file:
            level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
            file.write(f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n")
        print("The results are saved in \"results.txt\".")


if __name__ == "__main__":
    main()
