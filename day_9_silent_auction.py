import os
import day_9_gavel_art


bidding_dict = {}
continue_bidding = "yes"

print(day_9_gavel_art.logo)

while continue_bidding != "no":
	name = input("What is your name?\n")
	bid = int(input("What is your bid?\n"))
	bidding_dict[name] = bid

	continue_bidding = input("Are there any other bidders?\n").lower()
	os.system("clear")


highest_bid = 0
highest_bidder = ""

for bid in bidding_dict:
	if bidding_dict[bid] > highest_bid:
		highest_bid = bidding_dict[bid]
		highest_bidder = bid

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
