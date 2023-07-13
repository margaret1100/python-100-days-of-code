
import day_14_higher_lower_game_art
from os import system
from day_14_higher_lower_game_data import data
from random import randint


def get_account():

	number_of_accounts = len(data)
	account_number = randint(0, number_of_accounts - 1)
	account = data[account_number]
	return account


def compare_accounts(account_a, account_b, answer):
	
	system("clear")
	print(day_14_higher_lower_game_art.logo)

	if account_a["follower_count"] > account_b["follower_count"]:
		if answer == "a":
			return "correct"
		else:
			return "incorrrect"
	else:
		if answer == "b":
			return "correct"
		else:
			return "incorrrect"


def print_accounts(account):
	return (f"{account['name']}, {account['description']}, from {account['country']}")



def play_game():
	print(day_14_higher_lower_game_art.logo)
	score = 0

	my_account_a = get_account() 

	while True:
		my_account_b = get_account()

		# to not compare the same account to each other
		while my_account_a == my_account_b :
			my_account_b = get_account()

		print(f"Compare A: a {print_accounts(my_account_a)}")

		print(day_14_higher_lower_game_art.vs)

		print(f"Compare B: a {print_accounts(my_account_b)}")

		my_answer = input("who has more followers? Type 'A' or 'B':").lower()
		
		if compare_accounts(my_account_a, my_account_b, my_answer) == "correct":
			my_account_a = my_account_b
			score += 1
			print(f"You're Right! Current score: {score}")

		else:
			print(f"Sorry, that's wrong: Final score: {score}")
			return 





play_game()
