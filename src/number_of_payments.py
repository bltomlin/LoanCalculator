"""
This file contains the logic for calculating the monthly payment
when the period of the loan is known.
"""

import math

def number_of_payments(annuity_payment, loan_principal, nominal_interest):
	"""
	Calculates fixed monthly payment.

	:param: annuity_payment: fixed rate for monthly payments
	:param: loan_input: Dollar amount of the loan
	:param: nominal_interest: monthly interest rate
	:return: void
	"""
	n = math.log( 1 + i, annuity_payment / (annuity_payment - i * loan_principal) )
	return n