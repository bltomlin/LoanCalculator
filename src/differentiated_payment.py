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
    differentiated_payment = (loan_input / n) + i * (loan_input - ( (loan_input * (m - 1)) / n))
    return differentiated_payment