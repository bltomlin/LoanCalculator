"""
This file contains the logic for calculating the ordinary annuity (payment).
"""
from src import interest_rate_calculator

import math

def ordinary_annuity_calculator(loan_input, n , i):
	"""
	Calculates ordinary annuity (payment).

	:param: loan_input: principal loan
	:param: n: number of payments on the loan
	:param: i: monthly interest rate
	:return: calculated ordinary annuity
	"""
	i = interest_rate_calculator(i)
	ordinary_annuity = math.ceil(loan_input * ( (i * pow((1 + i), n)) / (pow((1+i), n) - 1 ) ) )
	return ordinary_annuity