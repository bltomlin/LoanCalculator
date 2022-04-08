def loan_principal(annuity_payment, nominal_interest):
	loan_principal = annuity_payment * ( (i * pow((1 + i), n) / (pow((1 + i), n) - 1) ))
	return loan_principal