"""Lunch: nice, cozy, tasty place"""

import random

def split_bill():

    try:
        num_friends = int(input("Enter the number of friends joining (including you):\n"))
        if num_friends <= 0:
            print("No one is joining for the party")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input().strip(): 0 for _ in range(num_friends)}

    try:
        total_amount = float(input("Enter the total amount:\n"))
        amount_per_person = round(total_amount / num_friends, 2)
        friends = {name: amount_per_person for name in friends}
    except ValueError:
        print("Invalid amount entered. Please enter a number.")
        return

    lucky_choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n").strip().lower()
    if lucky_choice == 'yes':
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        if num_friends > 1:
            new_amount_per_person = round(total_amount / (num_friends - 1), 2)
            friends = {name: new_amount_per_person if name != lucky_one else 0 for name in friends}
    elif lucky_choice == 'no':
        print("No one is going to be lucky")

    print(friends)

split_bill()
