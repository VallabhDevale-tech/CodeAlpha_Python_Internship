# Task 1: Hangman Game

A classic terminal-based Hangman game developed in Python as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Description

Hangman is an interactive, text-based word guessing game. The computer randomly selects a secret word from a predefined bank of words, representing hidden letters with underscores (`_`). The player attempts to guess the word one letter at a time within a limited number of incorrect attempts (maximum 6). For each incorrect guess, a visual ASCII-art representation of the hangman gallows progresses toward completion.

---

## 🚀 Features

- **Random Word Selection**: Words are chosen at random from a curated dictionary of computer and technology terms.
- **Dynamic Word Masking**: Displays blanks (`_`) for undiscovered letters and updates dynamically as correct letters are guessed.
- **ASCII Art Gallows**: Visual hangman rendering across 7 detailed stages (from empty gallows at 0 errors to full hangman figure at 6 errors).
- **Guess Tracking**: Displays all previously guessed letters in alphabetical order to avoid confusion.
- **Duplicate Guess Prevention**: Detects when a user repeats a letter and alerts them without penalty.
- **Robust Input Validation**:
  - Rejects numbers, special characters, and multi-character strings.
  - Case-insensitive (accepts lowercase or uppercase and processes uniformly).
- **Win / Loss Detection**:
  - Congratulates the player upon guessing all letters.
  - Displays game over and reveals the secret word if 6 incorrect attempts are reached.
- **Replay Loop**: Prompts the player to start a new game or exit gracefully when finished.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3.10+
- **Standard Library Modules**: `random`, `sys`
- **Interface**: Cross-platform Terminal / Command Line (VS Code Terminal, Command Prompt, PowerShell, Bash)

---

## 🧠 Python Concepts Demonstrated

1. **Random Module (`random.choice`)**: Used to pick unpredictable words for each session.
2. **Loops (`while` loops)**: Handles both the game state progression and the replay loop.
3. **Conditionals (`if`, `elif`, `else`)**: Evaluates player guesses, validates inputs, and triggers win/loss outcomes.
4. **Data Structures**:
   - `list`: Stores words and ordered ASCII art stages.
   - `set`: Stores unique guessed letters for fast $O(1)$ lookups and duplicate detection.
   - `str`: String manipulation, indexing, and slicing.
5. **Functions & Type Annotations**: Clean functional decomposition with type hints (`-> None`, `-> str`).
6. **Input Sanitation (`str.strip()`, `str.upper()`, `str.isalpha()`)**: Robust handling of user input.

---

## 📂 Project Structure

```text
Task_1_Hangman/
│
├── hangman.py          # Main executable Python game script
└── README.md           # Project documentation and instructions
```

---

## ⚙️ Installation & Prerequisites

1. Ensure **Python 3.10 or newer** is installed on your computer.
   Verify by running:
   ```bash
   python --version
   ```
2. No third-party packages are required. The game utilizes Python's built-in standard library.

---

## 🎮 How to Run the Project

1. Open your terminal or VS Code terminal.
2. Navigate to the project root directory or the task folder:
   ```bash
   cd Task_1_Hangman
   ```
3. Run the script:
   ```bash
   python hangman.py
   ```

---

## 🖥️ Sample Output

```text
=============================================
      WELCOME TO THE HANGMAN GAME!     
=============================================
Rules: Guess the secret word one letter at a time.
You can afford at most 6 incorrect guesses.

       +---+
       |   |
           |
           |
           |
           |
    =========

Word: _ _ _ _ _ _
----------------------------------------
Incorrect guesses: 0 / 6
Guessed letters: None
----------------------------------------
Enter your guess (a single letter): p

>> Good job! 'P' is in the word!


       +---+
       |   |
           |
           |
           |
           |
    =========

Word: P _ _ _ _ _
----------------------------------------
Incorrect guesses: 0 / 6
Guessed letters: P
----------------------------------------
Enter your guess (a single letter): z

>> Sorry! 'Z' is NOT in the word.


       +---+
       |   |
       O   |
           |
           |
           |
    =========

Word: P _ _ _ _ _
----------------------------------------
Incorrect guesses: 1 / 6
Guessed letters: P, Z
----------------------------------------
Enter your guess (a single letter): 
```

---

## 🏆 Internship Evaluation Checklist

- [x] Random word selection from predefined list
- [x] Underscores displayed for hidden letters
- [x] Guess one letter at a time with input validation
- [x] Track correct and incorrect guesses
- [x] Display ASCII hangman stages (0 to 6)
- [x] Prevent repeated guesses with friendly warning
- [x] Limit incorrect attempts to 6
- [x] Clear win and lose messages
- [x] Show correct word on loss
- [x] Replay game prompt (`y/n`)
