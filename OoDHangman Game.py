#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python Hangman!

import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

words = [
    'class', 'python', 'code', 'word', 'string', 'attribute'
]

class Hangman():
 

    def __init__(self, guessed_word):
        self.failed_attempts = 0
        self.guessed_word = guessed_word
        self.game_progress = list('_' * len(self.guessed_word))

    def find_indexes(self, letter):
      
        return [i for i, char in enumerate(self.guessed_word) if letter == char]

    def is_invalid_letter(self, input_):
      
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
        
        # We append withespaces both sides to make the game look prettier
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
     
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input

    def play(self):
      
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('¡The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('already guessed that letter')
                continue

            if user_input in self.guessed_word:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.guessed_word))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n¡OMG! You lost!")

if __name__ == '__main__':
    guessed_word = random.choice(words)
    hangman = Hangman(guessed_word)
    hangman.play()


# In[ ]:




