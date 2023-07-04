###### Number Guessing Game #####


import random
import day_12_number_guessing_art

def number_guessing():

	print(day_12_number_guessing_art.logo)

	rand_number = random.randint(1,100)

	print("I'm thinking of a number between 1 and 100")

	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

	if difficulty == "easy":
		lives = 10
	elif difficulty == "hard":
		lives = 5
	else:
		print("Invalid entry, please rerun game and enter 'easy' or 'hard'")
		return

	number_guessed = False

	while lives > 0 and number_guessed == False:
		print(f"You have {lives} attempts remaining to guess the number.")
		guessed_number = int(input("Make a guess: "))

		if guessed_number == rand_number:
			print(f"You got it! The answer was {rand_number}.")
			number_guessed = True
		elif guessed_number > rand_number:
			print("Too high.")
			lives -= 1
		else:
			print("Too low.")
			lives -= 1
		if lives > 0 and number_guessed == False:
			print("Guess again.")

	if lives == 0:
		print("You've run out of guesses, you lose")


number_guessing()