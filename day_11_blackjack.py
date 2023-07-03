############### Our Blackjack House Rules #####################

## Rules : The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import os
import day_11_blackjack_art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
	# Calculate score -  consider aces can be 1 or 11
	ace_counter = 0

	for card in cards:
		if card == 11:
			ace_counter += 1

	score = sum(cards)
	while ace_counter > 0 and score > 21:
		score -= 10
		ace_counter -= 1

	return score

def print_final_hands(player_list, dealer_list):
	# print final hands
	print(f"Your final hand: {player_list}: final score: {calculate_score(player_list)}")
	print(f"The Dealer's final hand: {dealer_list}: final score: {calculate_score(dealer_list)}")

def deal_card():
	# Deal a random card from the deck
	return random.choice(cards)

def black_jack():

	print(day_11_blackjack_art.logo)

	# Draw cards

	players_cards = []
	computer_cards = []

	# deal 2 cards to get started
	for _ in range(2):
		players_cards.append(deal_card())
		computer_cards.append(deal_card())

	print(f"Your cards: {players_cards}, current score: {calculate_score(players_cards)}")
	print(f"Computer's first card is: {computer_cards[0]}")

	draw_cards = True

	while draw_cards == True:
		print(f"Your cards: {players_cards}, current score: {calculate_score(players_cards)}")
		additional_card = input("Type 'y' to get another card, type 'n to pass:")

		if additional_card == 'n':
			draw_cards = False
			continue
		players_cards.append(deal_card())
		score = calculate_score(players_cards)
		if score > 21:
			print_final_hands(players_cards, computer_cards)
			result = "You lose, bust!"
			return result
		else:
			continue

	while calculate_score(computer_cards) < 17:
		computer_cards.append(deal_card())
		if calculate_score(computer_cards) > 21:
			print_final_hands(players_cards, computer_cards)
			result = "Dealer busts!"
			return result

	if calculate_score(computer_cards) > calculate_score(players_cards):
		result = "Dealer wins!"
	elif calculate_score(computer_cards) == calculate_score(players_cards):
		result = "Draw"
	else:
		result = "You win!"

	print_final_hands(players_cards, computer_cards)
	return result


while True:
	play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'".lower())

	if play_game == 'n':
		break
	else:
		os.system("clear")
		print(black_jack())





