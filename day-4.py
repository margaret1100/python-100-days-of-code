
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_selection = input("Please pick rock, paper, or scissors\n").lower()

print(f"You have choosen {player_selection}")

#find image for selection
if player_selection =='rock':
  print(rock)
elif player_selection == 'scissors':
  print(scissors)
elif player_selection == 'paper':
  print(paper)
else:
  print("Invalid selection, you lose")

computer_selection = random.randint(0,2)

if computer_selection == 0:
  print("The computer has chosen rock")
  print(rock)
  computer_selection_desc = 'rock'
elif computer_selection == 1:
  print("The computer has chosen paper")
  print(paper)
  computer_selection_desc  = 'paper'
else:
  print("The computer has chosen scissors")
  print(scissors)
  computer_selection_desc = 'scissors'

#Check if you win or lose
if player_selection == computer_selection_desc:
  print("Tie!")
elif player_selection == "rock" and computer_selection_desc == "scissors":
  print("You win!")
elif player_selection == "scissors" and computer_selection_desc == "paper":
  print("You win!")
elif player_selection == "paper" and computer_selection_desc == "rock":
  print("You win!")
else:
  print("You lose")

