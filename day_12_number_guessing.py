###### Number Guessing Game #####


import random
import day_12_number_guessing_art

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

	if difficulty == "easy":
		turns = EASY_LEVEL
	elif difficulty == "hard":
		turns = HARD_LEVEL
	return turns

def check_answer(guess, answer, turns):
	if guess > answer:
		print("Too high.")
		turns -= 1
	elif guess < answer:
		print("Too low.")
		turns -= 1
	else:
		print(f"You got it! The answer was {answer}.")
	return turns


def number_guessing():

	print(day_12_number_guessing_art.logo)

	rand_number = random.randint(1,100)

	print("I'm thinking of a number between 1 and 100")

	turns = set_difficulty()

	guessed_number = 0

	while guessed_number != rand_number:
		print(f"You have {turns} attempts remaining to guess the number.")
		guessed_number = int(input("Make a guess: "))

		turns = check_answer(guessed_number, rand_number, turns) 
		
		if turns == 0:
			print("You've run out of guesses, you lose")
			return
		elif guessed_number != rand_number:
			print("Guess again.")

number_guessing()
