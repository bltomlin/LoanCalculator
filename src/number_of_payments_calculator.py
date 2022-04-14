"""
This file contains the logic for calculating the number of payments until loan is paid off.
"""

from src import interest_rate_calculator

import math

def number_of_payments_calculator(loan_input, n , i):
	"""
	Calculates number of payments until loan is paid off.

	:param: loan_input: principal loan
	:param: n: number of payments on the loan
	:param: i: monthly interest rate
	:return: calculated number of payments in months
	"""
	i = interest_rate_calculator(i)
	number_of_payments = math.log((n / (n - (i * loan_input))), (1 + i))
	return number_of_payments