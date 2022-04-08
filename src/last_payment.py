"""
This file contains the logic to calculate the last months payment,
which is used if the remaining balance is less that the fixed monthly 
payment.
"""

def last_payment(loan_input, months_input, monthly_payment):
	"""
	Calculates payment for the last month. 
	
	:param loan_input: dollar amount of the loan
	:param months_input: user entered months desired to pay off loan
	:param monthly_payment: calculated fixed monthly pay rate
	:return: calculated last month payment
	"""
	last_payment = loan_input - (months_input - 1) * monthly_payment
	return last_payment