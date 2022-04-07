print("Enter the loan principal:")
loan_input = input()

print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
type_input = input()

if type_input == "m":
	print("Enter the monthly payment")
	monthly_input = input()
	months_needed = loan_input / monthly_input
	print(f"It will take {monthly_needed} months to repay the loan")
else:
	print("Enter the number of months")
	months_input = input()
	monthly_payment = loan_input / months_input
	print(f"Your monthly payment = {monthly_paymen}t")