from .context import anacondo
from . import generate_sample_block
import pytest
import numpy as np


@pytest.fixture
def sample_block():
	return generate_sample_block()

def test_loan_amount(sample_block):
	actual = np.round(sample_block.loan_amount(), 0)
	expected = 487500
	assert actual == expected

def test_monthly_payments(sample_block):
	actual = 2082
	expected = np.round(sample_block.monthly_payments(), 0)
	assert actual == expected

def test_annual_payments(sample_block):
	actual = 24980
	expected = np.round(sample_block.annual_payment(), 0)
	assert actual == expected

def test_mortgage_balance(sample_block):
	actual = [477491, 467167, 456518, 445534, 434205, 422520, 410467, 398036, 385213, 371988]
	expceted = np.round(sample_block.mortgage_balance(), 0)

def test_interest_paydown(sample_block):
	actual = [14971, 14656, 14332, 13997, 13651, 13295, 12928, 12549, 12158, 11755]
	expected = np.round(sample_block.interest_paydown()[0:10], 0)
	assert actual == list(expected)

def test_principal_paydown(sample_block):
	actual = [10009, 10324, 10649, 10984, 11329, 11685, 12053, 12432, 12823, 13226]
	expected = np.round(sample_block.principal_paydown()[0:10], 0)
	assert actual == list(expected)
