# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
___
## The Project
The game starts with the function 'play_game'. This function controls the flow and result of the game. 
At the start of the game, the computer randomly choses a word from a list of words. The player has a number of lives (default 5).
The game ends then the player wins or loses the game. 'play_game' continually calls the method 'ask_for_input', until the game ends.
The player wins the game by successfully selecting (guessing) all the letters in a randomly chosen word. Incorrect guesses result in the player losing a life. The player loses the game if they they lose all lives, before completing the word.

Importing 'random', the project selects a random word ('word') from a predefined list of words ('word_list').
The project then asks the user to guess a letter ('guess'). This is through the function 'ask_for_input()'.
'ask_for_input()' will loop until it receives valid input. Valid input is a single alphabetic letter.
'ask_for_input()' then checks if the letter is in the word by calling the function 'check_guess(guess)'.
'check_guess(guess)' reports if the letter is in the word or not.

___
## User Instructions
Start the game from the command line by typing 'python milestone_5.py'.
Follow the prompts to input single alphabetic letters. These selection are referred to as: 'guess'.
Continue to follow the prompts, until you win or lose the game.
You win by correctly completing (guessing), the word. If your guess is incorrect, you lose a life.
You lose the game by running out of lives, before you have guessed the word.



___
## License
This Hangman game is completely unlicensed and free for all to enjoy.
The concept, design and code are free from any intellectual property claim.
