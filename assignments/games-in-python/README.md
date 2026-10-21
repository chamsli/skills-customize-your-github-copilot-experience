
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice using strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word from a predefined list and prepare the game state so the player can begin guessing.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Track the letters the player has guessed and the number of incorrect guesses.
- Display the word's current progress with underscores for letters that have not been guessed (for example, `_ _ _`).


### 🛠️ Run the Guessing Game

#### Description
Use a loop to let the player guess letters until they reveal the secret word or run out of attempts.

#### Requirements
Completed program should:

- Accept letter guesses from the player and update the displayed progress when a guessed letter is in the secret word.
- Track and display how many incorrect guesses remain.
- End the game when the player guesses the word or reaches the maximum number of incorrect guesses.
- Display a win message when the player guesses the word and a lose message when the player runs out of attempts.
