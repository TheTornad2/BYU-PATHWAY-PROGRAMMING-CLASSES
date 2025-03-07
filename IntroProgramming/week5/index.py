import random

# Word Puzzle Game
# This program allows the user to guess a secret word with hints provided for incorrect guesses.

# List of words and their hints
word_list = {
    "mosiah": "This prophet was in the Old Testament.",
    "nephi": "He had a vision of the tree of life.",
    "alma": "This prophet was known for his preaching and conversion.",
    "helaman": "He was a military and spiritual leader in the Book of Mormon.",
    "enoch": "He built a city that was taken up to heaven."
}

# Randomly choose a secret word and its hint, this library is incredible.
secret_word = random.choice(list(word_list.keys()))
hint = word_list[secret_word]

def get_hint(secret, guess):
    hint = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            hint.append(guess[i].upper())  # Correct letter in the correct position
        elif guess[i] in secret:
            hint.append(guess[i].lower())  # Correct letter in the wrong position
        else:
            hint.append('_')  # Letter not in the secret word
    return ' '.join(hint)

guess_count = 0
correct_guess = False

print("Welcome to the word guessing game!")
print("Hint:", hint)  # Show initial hint
print("Your hint is:", "_ " * len(secret_word))  # Initial hint of underscores

while not correct_guess:
    guess = input("What is your guess? ").lower()  # Get user input and convert to lowercase
    guess_count += 1  # Increment guess count
    
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue  # Skip the rest of the loop
    
    if guess == secret_word:
        correct_guess = True  # User guessed correctly
        print(f"Congratulations! You guessed it!\nIt took you {guess_count} guesses.")
    else:
        hint_display = get_hint(secret_word, guess)  # Generate hint
        print("Your hint is:", hint_display)

