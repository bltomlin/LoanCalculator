"""
This file contains the logic for calculating the monthly payment
when the period of the loan is known.
"""
from src import last_payment

import math

def how_long_calculator(loan_input):
	"""
	Calculates fixed monthly payment.

	:param: loan_input: Dollar amount of the loan
	:return: void
	"""
	print("Enter the number of months")
	months_input = int(input())
	monthly_payment = math.ceil(loan_input / months_input)
	last_pay = last_payment(loan_input, months_input, monthly_payment)
	if last_pay != monthly_payment:
		print(f"Your monthly payment = {monthly_payment} and the last payment = {last_pay}")
	else:
		print(f"Your monthly payment = {monthly_payment}")