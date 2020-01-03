from .context import anacondo
import json
import numpy as np
import pytest
import os
import sys

def generate_sample_block():
	with open(os.path.join(sys.path[0], 'test/sample_data.json'), "r") as json_file:
		data = json.load(json_file)

	return anacondo.Blocks(**data['fake_test'])

@pytest.fixture
def sample_block():
	return generate_sample_block()

def test_generate_years(sample_block):
	assert range(1,11) == sample_block._generate_years()

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
	