from blocks import Blocks

# initiate variable values
property_value = 650000
purchase_price = 650000
interest_rate = 0.031
down_payment_pct = 0.25 
loan_term = 30
rental_income = 2700
vacancy=0
maintenance_reserve=0 
management_fee=0.15 
monthly_property_tax=167.0 
monthly_insurance=50.0
monthly_utility=90 
rental_income_increase=2 
property_tax_increase=2
closing_cost_buy=0.02
closing_cost_sell=0
years = 10

def sample_block():
	return Blocks(
	    property_value = property_value, 
	    purchase_price = purchase_price,
	    interest_rate = interest_rate, 
	    down_payment_pct = down_payment_pct, 
	    loan_term = loan_term,
	    rental_income = rental_income,
	    vacancy=vacancy, 
	    maintenance_reserve=maintenance_reserve, 
	    management_fee=management_fee, 
	    monthly_property_tax=monthly_property_tax, 
	    monthly_insurance=monthly_insurance,
	    monthly_utility=monthly_utility, 
	    rental_income_increase=rental_income_increase, 
	    property_tax_increase=property_tax_increase,
	    closing_cost_buy=closing_cost_buy, 
	    closing_cost_sell=closing_cost_sell,
	    years=10
	)