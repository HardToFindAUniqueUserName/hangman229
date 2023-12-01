import random

class Hangman:
    def __init__(self, word_list, number_of_lives = 5):
        """Parameters:"""
        self.word_list = word_list
        """word_list: list - A list of words"""
       
        self.number_of_lives = number_of_lives
        """number_of_lives: int - The number of lives the player has at the start of the game"""
        
        """Attributes:"""
        self.word = random.choice(word_list)
        """word: string - The word to be guessed, chosen randomly from word_list, using random.choice"""
        
        self.number_of_letters = len(set(self.word))
        """number_of_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        From self.word create a (unique) set. Measure length of set."""
        
        self.word_guessed = []
        """word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed"""
        for letter in self.word:
            self.word_guessed.append("_")
        
        self.list_of_guesses = []
        """list_of_guesses: list - A list of the guesses that have already been tried. Initialy set empty"""

    """Methods:
       check_letter(letter)
           Checks if the guessed letter is in the word.
       ask_letter()
           Asks the user to guess a letter.
    """
    def  check_guess(self, guess):
      """check_guess - Checks to see if the guess letter is in the word. If so update word_guessed and inform user.
      if not decrement number_of_lives and inform user"""
      if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        for index in range(len(self.word)):
           if guess == self.word[index]:
              self.word_guessed[index] = guess
        self.number_of_letters -= 1
      else:
        self.number_of_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.number_of_lives} left")

    def ask_for_input(self):
      """ask_for_input - Request single alpabetic letter as input. Validate and check not already used"""
      while True:
        guess = input("Make your guess by entering a single letter: ")
        guess = guess.lower()
        if not len(guess) == 1 or not guess.isalpha():
          print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
          print("You already tried that letter")
        else:
          self.check_guess(guess)
          self.list_of_guesses.append(guess)
          break

"""Functions:
   play_game(word_list)
      Start and controle the game. Action termination (win/loose)
"""
def play_game(word_list):
  '''This function is used to start and manage the game. It starts and continues successive turns by asking for input.
     It momitores the number of lives left and the number of letters left to find to continue or termiate the game.
     Args: word_list: list - (list of words available for project to make random choice
           number_of_lives: int - number of lives (possible failed guesses) available to the player.'''
  number_of_lives = 5
  game = Hangman(word_list, number_of_lives)
  while True:
    if game.number_of_lives == 0:
      print("You lost!")
      break
    elif game.number_of_letters > 0:
      game.ask_for_input()
    else:
         print("Congratulations. You won the game!")
         break
 
"""Entry point into game
""" 
if __name__ == '__main__':
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    """word_list: list - The list or woords from which the project will randomy choose a word to start the game"""
    play_game(word_list)


