"""
This file contains the logic for calculating the loan principal
when the annuity, number of payments and interest is known
"""

from src import interest_rate_calculator

def loan_principal_calculator(annuity_input, n , i):
	"""
	Calculates loan principal.

	:param: annuity_payment: fixed rate for monthly payments
	:param: n: number of payments on the loan
	:param: i: monthly interest rate
	:return: loan principal
	"""
	i = interest_rate_calculator(i)
	loan_principal = annuity_input / ( (i * pow((1 + i), n)) / (pow((1 + i), n) - 1 ) ) 
	return loan_principal