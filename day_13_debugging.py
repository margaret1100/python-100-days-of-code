############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21): # changed from 20 to 21
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # change range from (1,6) to (0,5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year >= 1980 and year < 1994: # added >= for 1980
  print("You are a millenial.")
elif year >= 1994: # added >= for 1994
  print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?")) # Added int
if age > 18:
  print(f"You can drive at age {age}.") # made F string

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: ")) # removed double equal
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # indented so it appends each for loop
  print(b_list)

mutate([1,2,3,5,8,13])


# Odd Even
number = int(input("Which number do you want to check?"))

if number % 2 == 0: # Fixed to add extra = sign for comparison
  print("This is an even number.")
else:
  print("This is an odd number.")
  

#Leap year code
year = int(input("Which year do you want to check?")) #converted input to int

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")