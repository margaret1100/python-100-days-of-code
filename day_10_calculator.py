
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


num1 = int(input("What is the first number?"))
num2 = int(input("what is the second number?"))

for function in function_dict:
	print(function)

operation = input("Pick an operation from the line above.")
answer = function_dict[operation](num1, num2)

print(f"{num1} {operation} {num2} = {answer}")

keep_calculating = True

while keep_calculating == True:
	calculating_decision = input("Would you like to continue calculating type y or n?")
	if calculating_decision.lower() == 'n':
		keep_calculating = False
		break

	for function in function_dict:
		print(function)

	operation = input("Pick an operation from the line above.")
	num3 = int(input("What is the next number?"))
	next_answer = function_dict[operation](answer, num3)
	
	print(f"{answer} {operation} {num3} = {next_answer}")

	answer = next_answer


