# Tip calculation

print("Welcome to the tip calculator")
total_bill = input("How much was the total bill?\n")
tip = input("How much would you like to tip 10, 12, 15?\n")
people = input("How many people are in the party?\n")


tip_as_percentage = int(tip)/100
total_bill_as_float = float(total_bill)
total_tip = tip_as_percentage * total_bill_as_float
people_as_int = int(people)
pay_per_person = (total_bill_as_float + total_tip)/people_as_int
amount_per_person_rounded = round(pay_per_person, 2)

print(f"${amount_per_person_rounded}")
