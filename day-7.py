import random

word_list = ["aardvark", "baboon", "camel"]

# pick a random word and assign it to chosen word
chosen_word = random.choice(word_list)

guess = input("Pick a letter\n").lower()

word_length = len(chosen_word)

hangman_list = []
# Create list with blanks to reprsent the random word
for n in range(word_length):
  hangman_list.append("_")

# check for match and replace matches with the guess
for position in range(word_length):
  if guess == chosen_word[position]:
    hangman_list[position] = guess

print(hangman_list)
