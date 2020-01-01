from .context import anacondo
# from sample_data.sample_block import sample_block
import numpy as np
import pytest


# @pytest.fixture
# def sample_block():
# 	return sample_block()

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

@pytest.fixture
def sample_block():
	return anacondo.Blocks(
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

def test_generate_years(sample_block):
	assert range(1,years+1) == sample_block._generate_years()

def test_capitalization_rate(sample_block):
	expected = [0.0367, 0.0375, 0.0383, 0.0391, 0.0399, 0.0408, 0.0417, 0.0425, 0.0434, 0.0444]
	actuals = sample_block.capitalization_rate()
	assert list(actuals) == expected

def test_return_on_equity(sample_block):
	expected = [0.0515, 0.0531, 0.0546, 0.0559, 0.0570, 0.0581, 0.0591, 0.0599, 0.0607, 0.0614]
	actuals = sample_block.return_on_equity()
	assert list(actuals) == expected

def test_cash_on_cash_return(sample_block):
	expected = [-0.0065, -0.0036, -0.0005, 0.0025, 0.0057, 0.0089, 0.0122, 0.0155, 0.0189, 0.0224]
	actuals = sample_block.cash_on_cash_return()
	assert list(actuals) == expected

def test_return_on_investment(sample_block):
	expected = [-0.005, 0.0514, 0.1126, 0.1789, 0.2504, 0.3271, 0.4093, 0.4970, 0.5903, 0.6895]
	actuals = sample_block.return_on_investment()
	assert list(actuals) == expected
	