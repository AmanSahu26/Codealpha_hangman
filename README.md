# 🎮 Hangman Game — CodeAlpha Python Internship Task 1

## 📌 Project Overview
A text-based Hangman game built in Python where the player guesses a hidden word one letter at a time. The game features ASCII art visuals that update with each wrong guess.

## 🚀 Features
- 5 predefined words chosen randomly each round
- ASCII art hangman that updates with every wrong guess
- Tracks correct and incorrect guesses separately
- Maximum 6 incorrect attempts allowed
- Replay option after each game ends
- Input validation (no duplicates, no numbers, single letter only)

## 🛠 Concepts Used
- `random` module
- `while` loop
- `if-elif-else` conditions
- Strings & Lists
- Functions

## 📁 File Structure
```
CodeAlpha_HangmanGame/
└── hangman.py
```

## ▶️ How to Run
```bash
python hangman.py
```

## 🎮 How to Play
1. Run the program
2. A random word is chosen (shown as underscores)
3. Guess one letter at a time
4. 6 wrong guesses = Game Over
5. Guess all letters correctly = You Win!

## 📸 Sample Output
```
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
=========

  Word:  p _ t h _ n

  Wrong Guesses (4/6): a, e, i, s

  Enter a letter: o
  ✅  'o' is in the word!
```

## 👤 Author
**Itachi** — CodeAlpha Python Programming Internship
