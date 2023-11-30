import random

word_list = ["apple", "banana", "cherry", "date", "elderberry"]

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        """Attribtes:"""
        self.word_list = word_list
        """word_list: list - A list of words"""
       
        self.num_lives = num_lives
        """num_lives: int - The number of lives the player has at the start of the game"""

        self.word = random.choice(word_list)
        """word: string - The word to be guessed, chosen randomly from word_list, using random.choice"""
        print(self.word)
        
        self.num_letters = len(set(self.word))
        """num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        From self.word create a (unique) set. Measure length of set."""
        print(self.num_letters)
        
        self.word_guessed = []
        """word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed"""
        for letter in self.word:
            self.word_guessed.append("_")
        
        self.list_of_guesses = []
        """list_of_guesses: list - A list of the guesses that have already been tried. Initialy set empty"""

    """Methods"""
    def  check_guess(self, guess):
      """check_guess - Checks to see if the guess letter is in the word. If so update word_guessed and inform user.
      if not decrement num_lives and inform user"""
      if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        for i in range(len(self.word)):
           if guess == self.word[i]:
              self.word_guessed[i] = guess
              print(self.word_guessed)
        self.num_letters -= 1
      else:
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} left")

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


hm1 = Hangman(word_list)
hm1.ask_for_input()


