#Create a hangman game

import random

word_list = ["aardvark", "baboon", "camel"]

# pick a random word and assign it to chosen word
chosen_word = random.choice(word_list)

guess = input('Pick a letter\n').lower()

# iterate through word to check for match
for n in range(len(chosen_word)):
  if guess == chosen_word[n]:
    print('match')
  else:
    print('no match')
