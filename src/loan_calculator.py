"""
This file contains the main entry point for the program that
dictates all logical flow.
"""
import argparse
from src import what_calculate, number_of_payments_calculator, ordinary_annuity_calculator, loan_principal_calculator

def loan_calculator():
	"""
	Entry point for program.

	:return: void
	"""
	parser = argparse.ArgumentParser(description="This program calculates loan payments.")
	parser.add_argument("--type")
	parser.add_argument("--payment")
	parser.add_argument("--principal") 
	parser.add_argument("--periods") 
	parser.add_argument("--interest") 
	args = parser.parse_args()
	data = [args.payment, args.principal, args.periods, args.interest]
	if args.type == "annuity":
		if args.principal != None and args.payment != None and args.interest != None:
			number_of_payments = math.ceil(number_of_payments_calculator(int(args.principal), int(args.payment) , float(args.interest)))
			remainder = int(number_of_payments % 12)
			years = int(number_of_payments / 12)
			print(f"It will take {years} years and {remainder} months to repay this loan!")
		elif args.principal != None and args.periods != None and args.interest != None:
			orindary_annuity = ordinary_annuity_calculator(int(args.principal), int(args.periods) , float(args.interest))
			print(f"Your monthly payment = {orindary_annuity}")
		else:
			loan_principal = math.floor(loan_principal_calculator(int(args.payment), int(args.periods) , float(args.interest)))
			print(f"Your loan principal = {loan_principal}!")


if __name__ == '__main__':
    loan_calculator()