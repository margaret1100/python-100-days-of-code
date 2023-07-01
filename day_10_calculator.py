
import day_10_calc_logo

# Create add, subtract, multiply, and divide functions

def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2


function_dict = { 
	"+": add,
  	"-" : subtract,
  	"x" : multiply, 
  	"/" : divide
}

def calculator():
	print(day_10_calc_logo.logo)
	num1 = float(input("What is the first number?"))
	keep_calculating = True


	while keep_calculating == True:
		for function in function_dict:
			print(function)

		operation = input("Pick an operation from the line above.")
		num2 = float(input("what is the next number?"))

		answer = function_dict[operation](num1, num2)

		print(f"{num1} {operation} {num2} = {answer}")

		continue_calc = input(f"Would you like to continue calculating with {answer} type 'y' or start a new calculation type 'n'")

		if continue_calc == 'n':
			calculator()
		else:
			num1 = answer

calculator()