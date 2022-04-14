"""
This file contains the main entry point for the program that
dictates all logical flow.
"""
from src import what_calculate, number_of_payments_calculator, ordinary_annuity_calculator, loan_principal_calculator

def loan_calculator():
	"""
	Entry point for program.

	:return: void
	"""
	type_input = what_calculate()
	
	if type_input == "n":
		print("Enter the loan principal:")
		loan_input = int(input())
		print("Enter the monthly payment:")
		n = int(input())
		print("Enter the loan interest:")
		i = float(input())
		number_of_payments = math.ceil(number_of_payments_calculator(loan_input, n , i))
		remainder = int(number_of_payments % 12)
		years = int(number_of_payments / 12)
		print(f"It will take {years} years and {remainder} months to repay this loan!")
	elif type_input == "a":
		print("Enter the loan principal:")
		loan_input = int(input())
		print("Enter the number of periods:")
		n = int(input())
		print("Enter the loan interest:")
		i = float(input())
		orindary_annuity = ordinary_annuity_calculator(loan_input, n , i)
		print(f"Your monthly payment = {orindary_annuity}")
	else:
		print("Enter the annuity payment:")
		annuity_input = float(input())
		print("Enter the number of periods:")
		n = int(input())
		print("Enter the loan interest:")
		i = float(input())
		loan_principal = loan_principal_calculator(annuity_input, n , i)
		print(f"Your loan principal = {loan_principal}!")
	    

if __name__ == '__main__':
    loan_calculator()