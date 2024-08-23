# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:06:46 2024

@author: zohai
"""

import random

words = ['turducken', 'dormamu', 'meowscles', 'mugiwara no luffy', 'runescape', 'pc'] #list

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word] # Create list of underscores
attempts = 10 # Number of attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word): #enumerate takes chosen word and gives access to letter and index of letter
            if letter == guess:
                word_display[index] = guess # reveal letter
    else: 
        print("That letter is not in the word.")
        attempts -= 1
        
# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You suck!")