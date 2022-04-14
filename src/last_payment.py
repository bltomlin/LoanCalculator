"""
This file contains the logic to calculate the last months payment,
which is used if the remaining balance is less that the fixed monthly 
payment.
"""

import math

def last_payment(loan_input, n, i):
	"""
	Calculates last payment.

	:param: loan_input: principal loan
	:param: n: number of payments on the loan
	:param: i: monthly interest rate
	:return: calculated last payment
	"""
	last_payment = math.ceil(loan_input - (n - 1) * i)
	return last_payment