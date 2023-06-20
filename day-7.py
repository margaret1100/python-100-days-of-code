#Step 3

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["aardvark", "baboon", "camel"]

# pick a random word and assign it to chosen word
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
# Create list to put letter display
display = []
for n in range(word_length):
    display.append("_")

lives = 6
end_of_game = False

while end_of_game == False:
    guess = input("Pick a letter\n").lower()

    if guess in chosen_word and guess not in display:
        # check for match and replace matches with the guess
        for position in range(word_length):
            if guess == chosen_word[position]:
                display[position] = guess
        blanks_left = display.count('_')
        print(display)
        # Check if word has been solved.
        if '_' not in display:
            end_of_game = True
            print('You won!')
    else:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lose!')
