"""
=============================================================================
Project 1: Hangman Game
Author: CodeAlpha Python Internship
Description: A classic terminal-based Hangman game built with Python.
             Players guess a randomly chosen word letter-by-letter with a
             maximum of 6 incorrect attempts before the hangman is complete.
=============================================================================
"""

import random

# Predefined list of secret words with hint hints/categories for better UX
WORD_BANK = [
    "PYTHON", "DEVELOPER", "ALGORITHM", "VARIABLE", "FUNCTION",
    "KEYBOARD", "COMPUTER", "DATABASE", "SOFTWARE", "INTERNSHIP",
    "NETWORK", "SECURITY", "BROWSER", "TERMINAL", "PROGRAMMING"
]

# Maximum allowed incorrect guesses
MAX_INCORRECT_ATTEMPTS = 6

# ASCII art stages representing the gallows from 0 to 6 incorrect guesses
HANGMAN_STAGES = [
    # Stage 0: 0 incorrect guesses (Empty gallows)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # Stage 1: 1 incorrect guess (Head)
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # Stage 2: 2 incorrect guesses (Head + Torso)
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # Stage 3: 3 incorrect guesses (Head + Torso + Left Arm)
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # Stage 4: 4 incorrect guesses (Head + Torso + Both Arms)
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # Stage 5: 5 incorrect guesses (One Leg)
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # Stage 6: 6 incorrect guesses (Full body - Game Over)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def get_random_word(word_list: list[str]) -> str:
    """Randomly select a word from the provided list and return it in uppercase."""
    return random.choice(word_list).upper()


def display_game_status(secret_word: str, guessed_letters: set[str], incorrect_count: int) -> None:
    """
    Display the current ASCII hangman stage, the masked secret word,
    and a summary of guessed letters and remaining attempts.
    """
    print(HANGMAN_STAGES[incorrect_count])

    # Build the masked word string with spaces between characters
    revealed_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {revealed_word}")
    print("-" * 40)
    print(f"Incorrect guesses: {incorrect_count} / {MAX_INCORRECT_ATTEMPTS}")
    
    # Display previously guessed letters sorted alphabetically
    if guessed_letters:
        sorted_guesses = ", ".join(sorted(guessed_letters))
        print(f"Guessed letters: {sorted_guesses}")
    else:
        print("Guessed letters: None")
    print("-" * 40)


def get_valid_letter_guess(guessed_letters: set[str]) -> str:
    """
    Prompt the player for a guess and ensure input validity:
    - Must be a single character
    - Must be an alphabetic letter
    - Must not have been guessed already
    """
    while True:
        user_input = input("Enter your guess (a single letter): ").strip().upper()

        if len(user_input) != 1 or not user_input.isalpha():
            print(">> Invalid input! Please enter a single alphabetic letter (A-Z).\n")
            continue

        if user_input in guessed_letters:
            print(f">> You have already guessed '{user_input}'. Try a different letter!\n")
            continue

        return user_input


def play_game() -> None:
    """Run a single round of the Hangman game."""
    secret_word = get_random_word(WORD_BANK)
    guessed_letters: set[str] = set()
    incorrect_count = 0

    print("\n" + "=" * 45)
    print("      WELCOME TO THE HANGMAN GAME!     ")
    print("=" * 45)
    print("Rules: Guess the secret word one letter at a time.")
    print(f"You can afford at most {MAX_INCORRECT_ATTEMPTS} incorrect guesses.")

    # Game loop continues until the word is guessed or max attempts are reached
    while incorrect_count < MAX_INCORRECT_ATTEMPTS:
        display_game_status(secret_word, guessed_letters, incorrect_count)

        # Check if all letters in the secret word have been guessed
        word_completed = all(letter in guessed_letters for letter in secret_word)
        if word_completed:
            print("\n" + "*" * 45)
            print(f" CONGRATULATIONS! YOU WON! ")
            print(f" The secret word was: {secret_word}")
            print("*" * 45 + "\n")
            return

        # Get player's next valid guess
        guess = get_valid_letter_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"\n>> Good job! '{guess}' is in the word!\n")
        else:
            incorrect_count += 1
            print(f"\n>> Sorry! '{guess}' is NOT in the word.\n")

    # Final check if loop exited due to hitting max incorrect attempts
    display_game_status(secret_word, guessed_letters, incorrect_count)
    print("\n" + "!" * 45)
    print(" GAME OVER! You ran out of attempts.")
    print(f" The correct word was: {secret_word}")
    print("!" * 45 + "\n")


def main() -> None:
    """Main function containing the replay loop."""
    while True:
        play_game()

        # Ask if the player wants to replay
        while True:
            choice = input("Would you like to play again? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                print("\nStarting a new game...")
                break
            elif choice in ("n", "no"):
                print("\nThank you for playing Hangman! Goodbye!\n")
                return
            else:
                print(">> Please enter 'y' for Yes or 'n' for No.")


if __name__ == "__main__":
    main()
