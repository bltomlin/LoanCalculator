"""
This file contains the logic to calculate a differentiated payment.
"""

def differentiated_payments_calculator(loan_input, n, i, m):
    """
    Calculates differentiated payment.

    :param: loan_input: principal loan
    :param: n: number of payments on the loan
    :param: i: monthly interest rate
    :return: calculated last payment
    """
    m = 1
    i = i / (12 * 100)
    differentiated_payment_total = 0
    loan_principal = math.floor(loan_principal_calculator(loan_input, n, i))
    while m <= n:
	    differentiated_payment = math.floor((loan_principal / n) + i * (loan_principal - ( (loan_principal * (m - 1)) / n)))
	    differentiated_payment_total += differentiated_payment
	    print("Month " + str(m) + ": payment is " + str(differentiated_payment))
	    m += 1
    overpayment = math.floor(differentiated_payment_total - loan_principal)
    print("Overpayment = " + str(overpayment))