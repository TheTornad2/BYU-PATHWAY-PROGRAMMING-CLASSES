# CSE 110 - Project 04: Word Puzzle with Hangman-style gameplay


"""

This is my final project for the week 4, the first time I readed the lessons and saw the videos I was thinking on the Hangman game, this is litteraly a hangman game becase I thout the example was going to be perfect.

I donwloaded the ASCII on Github and started to make it true.

I hope you enjoy it.


"""

import random

# List of possible secret words (Prophets' names)
secret_words = ["mosiah", "nephi", "helaman", "moroni", "Limhi", "Noah", "Peter"]
# Secret word stored (randomly selected)
secret_word = random.choice(secret_words).lower()

# Hangman ASCII art for incorrect guesses
HANGMANPICS = [
    """  
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


# Function to display the current hangman state based on incorrect guesses
def display_hangman(incorrect_guesses_count):
    print(HANGMANPICS[incorrect_guesses_count])


# Function to display the current progress of the word with correctly guessed letters
def display_current_progress(secret_word, correct_guesses):
    progress = []
    for letter in secret_word:
        if letter in correct_guesses:
            progress.append(letter.upper())
        else:
            progress.append("_")
    return " ".join(progress)


# Welcome message
print("Welcome to the Hangman-style word guessing game with prophets!")

# Initialize game variables
max_incorrect_guesses = (
    len(HANGMANPICS) - 1
)  # Number of incorrect guesses before losing (7 stages)
incorrect_guesses_count = 0  # Track how many incorrect guesses
guesses = 0  # Total guess count
correct_guesses = []  # Track letters guessed correctly
incorrect_guesses = []  # Track incorrect guesses

# Game loop
while incorrect_guesses_count < max_incorrect_guesses:
    # Display the current hangman state
    display_hangman(incorrect_guesses_count)

    # Display current progress of the word
    print(f"\nCurrent word: {display_current_progress(secret_word, correct_guesses)}")
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")

    # Prompt the user for a guess
    guess = input("Guess a letter: ").lower()

    # Make sure the guess is valid (one letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please guess a single letter.")
        continue

    # Increment guess count
    guesses += 1

    # Check if the guess is in the secret word
    if guess in secret_word:
        if guess not in correct_guesses:
            correct_guesses.append(guess)  # Add correct guess
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            print(f"You've already guessed the letter '{guess}'.")
    else:
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)  # Add incorrect guess
            incorrect_guesses_count += 1  # Increase hangman stage
            print(f"Sorry, the letter '{guess}' is not in the word.")
        else:
            print(f"You've already guessed the letter '{guess}' incorrectly.")

    # Check if the player has guessed the entire word
    if all(letter in correct_guesses for letter in secret_word):
        print(
            f"\nCongratulations! You've guessed the word '{secret_word.upper()}' correctly!"
        )
        print(f"It took you {guesses} guesses.")
        break

# If player runs out of lives (incorrect guesses)
if incorrect_guesses_count == max_incorrect_guesses:
    display_hangman(incorrect_guesses_count)
    print(
        f"\nGame over! You've run out of lives. The correct word was '{secret_word.upper()}'."
    )
