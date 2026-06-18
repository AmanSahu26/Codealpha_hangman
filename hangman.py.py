# ============================================================
#   CODEALPHA INTERNSHIP — TASK 1
#   Project  : Hangman Game
#   Author   : Itachi
#   Platform : CodeAlpha Python Programming Internship
# ============================================================

import random

# ---------- ASCII Art for Hangman Stages ----------
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# ---------- Predefined Word List ----------
WORDS = ["python", "hangman", "coding", "laptop", "science"]

# ---------- Game Functions ----------

def choose_word():
    """Randomly select a word from the list."""
    return random.choice(WORDS)

def display_board(stage, word, guessed_letters, wrong_letters):
    """Print current game state."""
    print(HANGMAN_STAGES[stage])
    print("\n  Word: ", end="")
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    print(f"\n  Wrong Guesses ({len(wrong_letters)}/6): {', '.join(wrong_letters) if wrong_letters else 'None'}")
    print()

def get_guess(guessed_letters):
    """Get a valid single letter guess from the user."""
    while True:
        guess = input("  Enter a letter: ").strip().lower()
        if len(guess) != 1:
            print("  ⚠  Please enter only ONE letter.")
        elif not guess.isalpha():
            print("  ⚠  Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print("  ⚠  You already guessed that letter! Try again.")
        else:
            return guess

def play_game():
    """Main game loop."""
    print("\n" + "="*45)
    print("       🎮  WELCOME TO HANGMAN GAME  🎮")
    print("="*45)
    print("  Guess the word before the man is hanged!")
    print("  You have 6 incorrect guess attempts.\n")

    word           = choose_word()
    guessed_letters = []
    wrong_letters   = []
    max_wrong       = 6

    while True:
        display_board(len(wrong_letters), word, guessed_letters, wrong_letters)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("  🎉  YOU WIN! The word was:", word.upper())
            break

        # Check loss condition
        if len(wrong_letters) >= max_wrong:
            print(f"\n  💀  GAME OVER! The word was: {word.upper()}")
            break

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"\n  ✅  '{guess}' is in the word!\n")
        else:
            wrong_letters.append(guess)
            remaining = max_wrong - len(wrong_letters)
            if remaining > 0:
                print(f"\n  ❌  '{guess}' is NOT in the word! {remaining} attempt(s) left.\n")

def main():
    """Entry point — allows replaying."""
    while True:
        play_game()
        again = input("\n  Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing Hangman! Goodbye! 👋\n")
            break

# ---------- Run ----------
if __name__ == "__main__":
    main()
