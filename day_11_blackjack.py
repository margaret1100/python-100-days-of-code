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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
	ace_counter = 0

	for card in cards:
		if card == 11:
			counter += 1

	score = sum(cards)
	if score > 21 and ace_counter > 0:
		while score > 21:
			score -= 10
			ace_counter -= 1
	return score

def black_jack():

	play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'".lower())

	if play_game == 'n':
		play_game = 'n'
		return play_game

	# Draw cards

	players_cards = [random.choice(cards), random.choice(cards)]

	computer_cards = [random.choice(cards), random.choice(cards)]

	print(f"Your cards: {players_cards}, current score: {calculate_score(players_cards)}")
	print(f"Computer's first card is: {computer_cards[0]}")

	draw_cards = True

	while draw_cards == True:
		print(f"Your cards: {players_cards}, current score: {calculate_score(players_cards)}")
		additional_card = input("Type 'y' to get another card, type 'n to pass:")

		if additional_card == 'n':
			draw_cards = False
			continue
		players_cards.append(random.choice(cards))
		score = calculate_score(players_cards)
		if score > 21:
			result = "You lose, bust!"
			return result
		else:
			continue

	while calculate_score(computer_cards) < 17:
		computer_cards.append(random.choice(cards))
		if calculate_score(computer_cards) > 21:
			result = "Dealer busts!"
			return result

	if calculate_score(computer_cards) > calculate_score(player_cards):
		result = "Dealer wins with {calculate_score(computer_cards)}"
	elif calculate_score(computer_cards) == calculate_score(player_cards):
		result = "Draw"
	else:
		result = "Player wins with {calculate_score(player_cards)}"

	return result


print(black_jack())





