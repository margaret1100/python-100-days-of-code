
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_together = name1 + name2
names_together_lower = names_together.lower()

true_count = names_together_lower.count('t') + names_together_lower.count('r') + names_together_lower.count('u') + names_together_lower.count('e')
love_count = names_together_lower.count('l') + names_together_lower.count('o') + names_together_lower.count('v') + names_together_lower.count('e')

put_together = str(true_count) + str(love_count)
put_together_int = int(put_together)

if put_together_int < 10 or put_together_int > 90:
    print(f"Your score is {put_together}, you go together like coke and mentos.")
elif put_together_int >= 40 and put_together_int <= 50:
    print(f"Your score is {put_together}, you are alright together.")
else:
    print(f"Your score is {put_together}")