"""
This file contains the logic for calculating the ordinary annuity.
"""

def ordinary_annuity(loan_input, nominal_interest):
	"""
	Calculates the ordinary annuity.

	:param: loan_input: dollar amount of the loan
	:param: nominal_interest: monthly interest rate
	:return: void
	"""
	ordinary_annuity = loan_input * ( (i * pow((1 + i), n) / (pow((1 + i), n) - 1) )