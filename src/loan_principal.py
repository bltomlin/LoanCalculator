"""
This file contains the logic for calculating the monthly payment
when the period of the loan is known.
"""

def loan_principal(annuity_payment, nominal_interest):
	"""
	Calculates fixed monthly payment.

	:param: loan_input: Dollar amount of the loan
	:return: monthly payment required by user
	"""
	loan_principal = annuity_payment * ( (i * pow((1 + i), n) / (pow((1 + i), n) - 1) ))
	return loan_principal