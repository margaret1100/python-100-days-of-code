# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#initialize variables

password_list = []

password = ''

for letters_list_len in range(0, nr_letters):
    password_list.append(random.choice(letters))

for numbers_list_len in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for symbols_list_len in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for element in password_list:
    password += str(element)

print(f'Easy password is {password}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#track random order list len 
random_order_list_len = 0
random_order_list = []
password_list_len = len(password_list) 

# A list shuffle could be used
while random_order_list_len < password_list_len:
    rand_nr = random.randint(0, password_list_len-1)
    if rand_nr not in random_order_list:
        random_order_list.append(rand_nr)
    random_order_list_len = len(random_order_list)

hard_password = ''

for number in random_order_list:
    hard_password += str(password_list[number])

print(f'Hard password is {hard_password}')


