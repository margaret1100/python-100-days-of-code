#Step 3

import random
import day_7_ascii_art
import day_7_word_list
import os

print(day_7_ascii_art.logo)

# pick a random word and assign it to chosen word
chosen_word = random.choice(day_7_word_list.word_list)

word_length = len(chosen_word)

# Create list to put letter display
display = []
for n in range(word_length):
    display.append("_")

lives = 6
end_of_game = False
guess_list = []


while end_of_game == False:

    guess = input("Pick a letter\n").lower()

    #clear screen to avoid buildup of guesses
    os.system("clear")
    

    if guess in chosen_word and guess not in display:

        print(f"You picked the letter {guess}, it is in the word\n")
        
        # check for match and replace matches with the guess
        for position in range(word_length):
            if guess == chosen_word[position]:
                display[position] = guess
        blanks_left = display.count('_')

        day_7_ascii_art.stages[lives]

        # Check if word has been solved.
        if '_' not in display:
            end_of_game = True
            print("You won!")
    
    elif guess in guess_list:

      print(f"You picked the letter {guess}, you have already chosen this letter\n")


    else:

        lives -= 1

        print(f"You picked the letter {guess}, it is not in the word. You have {lives} lives left\n")
        

        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was {chosen_word}")

    print("".join(display))

    print(day_7_ascii_art.stages[lives])

    guess_list.append(guess)

    print(f"You have guessed the following letters so far {','.join(guess_list)}")
    
