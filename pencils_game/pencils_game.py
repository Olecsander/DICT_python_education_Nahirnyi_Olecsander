"""Marco: smart interesting game"""

import random


def get_pencils():
    while True:
        pencils = input("How many pencils would you like to use:\n> ")
        if pencils.isdigit() and int(pencils) > 0:
            return int(pencils)
        print("The number of pencils should be numeric and positive")


def get_first_player():
    while True:
        first_player = input("Who will be the first (John, Jack):\n> ")
        if first_player in ["John", "Jack"]:
            return first_player
        print("Choose between 'John' and 'Jack'")


def print_pencils(pencils):
    print('|' * pencils)


def bot_turn(pencils):
    if pencils == 1:
        return 1
    elif pencils % 4 == 1:
        return  random.randint(1, 3)
    elif pencils % 4 == 0:
        return 3
    elif pencils % 4 == 2:
        return 1
    elif pencils % 4 == 3:
        return 2


def player_turn(pencils, current_player):
    while True:
        taken = input(f"{current_player}'s turn:\n> ")
        if taken in ["1", "2", "3"] and int(taken) <= pencils:
            return int(taken)
        elif taken not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
        else:
            print("Too many pencils were taken")


def game():
    pencils = get_pencils()
    current_player = get_first_player()
    print_pencils(pencils)

    while pencils > 0:
        if current_player == "Jack":
            taken = bot_turn(pencils)
            print(f"Jack's turn:\n{taken}")
        else:
            taken = player_turn(pencils, current_player)

        pencils -= taken
        print_pencils(pencils)

        current_player = "John" if current_player == "Jack" else "Jack"

        if pencils == 0:
            print(f"{current_player} won!")


game()
