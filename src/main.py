"""
This file contains the main entry point for the program that
dictates all logical flow.
"""
from src import period_calculator, how_long_calculator

def loan_calculator():
	"""
	Entry point for program.

	:return: void
	"""

	print("Enter the loan principal:")
	loan_input = int(input())

	print("What do you want to calculate?")
	print('type "m" - for number of monthly payments,')
	print('type "p" - for the monthly payment:')
	type_input = str(input())

	if type_input == "m":
		period_calculator()
	else:
	    how_long_calculator(loan_input)
	    

if __name__ == '__main__':
    honest_calculator()