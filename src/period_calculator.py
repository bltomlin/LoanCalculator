"""
This file contains the logic for calculating how it will take to
repay the loan in full if the user knows the amount of the monthly
repayments.
"""

import math

def period_calculator():
	"""
	Calculating time to repay loan in full.

	:return: void
	"""
	print("Enter the monthly payment")
	monthly_input = int(input())
	months_needed = math.ceil(loan_input / monthly_input)
	if months_needed < 2:
		print(f"It will take {months_needed} month to repay the loan")
	else:
		print(f"It will take {months_needed} months to repay the loan")