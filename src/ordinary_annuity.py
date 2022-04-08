def ordinary_annuity(loan_input, nominal_interest):
	ordinary_annuity = loan_input * ( (i * pow((1 + i), n) / (pow((1 + i), n) - 1) )