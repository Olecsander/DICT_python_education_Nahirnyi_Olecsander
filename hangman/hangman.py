"""Game: an interesting and educational"""

print("HANGMAN\nThe game will be available soon.")
import random
def guess_letters_with_validation():
    words_list = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words_list)
    display = "-" * len(secret_word)
    attempts = 8
    guessed_letters = set()
    while attempts > 0 and "-" in display:
        print(display)
        guess = input("Input a letter: > ")
        if len(guess) != 1 or not guess.islower():
            print("Please enter a lowercase English letter.")
        elif guess in guessed_letters:
            print("You've already guessed this letter.")
        elif guess in secret_word:
            guessed_letters.add(guess)
            display = "".join([guess if secret_word[i] == guess else display[i] for i in range(len(secret_word))])
        else:
            print("That letter doesn't appear in the word")
            guessed_letters.add(guess)
            attempts -= 1
    if "-" not in display:
        print("You guessed the word!\nYou survived!")
    else:
        print("You lost!")

guess_letters_with_validation()
def hangman_game():
    while True:
        choice = input('HANGMAN\nType "play" to play the game, "exit" to quit: > ')
        if choice == "play":
            guess_letters_with_validation()
        elif choice == "exit":
            break
hangman_game()
