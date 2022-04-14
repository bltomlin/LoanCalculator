"""
This file contains the logic to calculate the interest rate.
"""

def interest_rate_calculator(i):
	"""
	param: i: loan interest
	return: calculated interest rate
	"""
	i = i / (12 * 100)
	return i