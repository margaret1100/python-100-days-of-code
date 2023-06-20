#Step 3

import random

word_list = ["aardvark", "baboon", "camel"]

# pick a random word and assign it to chosen word
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
# Create list to put letter display
display = []
for n in range(word_length):
  display.append("_")

blanks_left = display.count('_')

while blanks_left > 0:
  guess = input("Pick a letter\n").lower()
  
  # check for match and replace matches with the guess
  for position in range(word_length):
    if guess == chosen_word[position]:
      display[position] = guess
  blanks_left = display.count('_')
  print(display)  
  

