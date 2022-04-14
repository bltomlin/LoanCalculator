"""
This file contains the logic for prompting the user menu.
"""

def what_calculate():
	"""
	Prompts the user with question and returns user input.

	:param: void
	:return: user input
	"""
	print("What do you want to calculate?")
	print('type "n" for number of monthly payments,')
	print('type "a" for annuity monthly payment amount,')
	print('type "p" for loan principal:')
	user_input = str(input())
	return user_input
