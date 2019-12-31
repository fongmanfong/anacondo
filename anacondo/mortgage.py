import numpy as np
import numpy_financial as npf
import pandas as pd

# years should be Print eventually probably

class Mortgage(object):

	"""
    This class creates a Mortgage object that contains mortgage related information such as 
    mortgage balance, interest payments, and principal accumulated.

    Parameters
    -----------
    purchase_print: float
      The purchase price of the real estate property. 
    interest_rate: float,
      The interest rate of the mortgage. Values between 0 and 1
    down_payment_pct: float
      The percentage of down payment made on the real estate property. Values between 0 and 1
    loan_term: integer
      The number of years for the mortgage
    """

	def __init__(self, purchase_price, interest_rate, down_payment_pct, loan_term, years=30):
		self.interest_rate = interest_rate
		self.down_payment_pct = down_payment_pct
		self.loan_term = loan_term
		self.purchase_price = purchase_price
		self.years=years

	def _generate_years(self):
		return range(1,self.years+1)

	def _cumulative_principal_or_interest(self, start, end, rate, nper, pv, func):
		# func: np.ppmt or np.ipmt
		cp = 0
		for i in range(start,end+1):
			cp = cp + (-func(rate / 12, i, nper*12, pv))
		return cp

	def _paydown(self, func):
		# func: cumulative_principal or cumulative_interest
		return np.array([func(i*12-11, i*12, self.interest_rate, self.loan_term, self.loan_amount()) for i in self._generate_years()])

	def cumulative_principal(self, start, end, rate, nper, pv):
		return self._cumulative_principal_or_interest(start, end, rate, nper, pv, npf.ppmt)

	def cumulative_interest(self, start, end, rate, nper, pv):
		return self._cumulative_principal_or_interest(start, end, rate, nper, pv, npf.ipmt)

	def loan_amount(self):
		return self.purchase_price * (1 - self.down_payment_pct)

	def monthly_payments(self):
		return -np.pmt(self.interest_rate / 12.0, self.loan_term * 12, self.loan_amount())

	def annual_payment(self):
		return self.monthly_payments()*12

	def mortgage_balance_summary(self):
		return pd.DataFrame({
			'Year': [i for i in self._generate_years()],
			'Total Paid': [self.annual_payment() for i in self._generate_years()],
			'Mortgage Balance': self.mortgage_balance(),
			'Principal Paydown': self.principal_paydown(),
			'Interest Paydown': self.interest_paydown(),
		})

	def mortgage_balance(self):
		return np.array([round(np.fv(self.interest_rate / 12.0, i*12, self.monthly_payments(), -self.loan_amount()), 2) for i in self._generate_years()])

	def principal_paydown(self):
		return self._paydown(self.cumulative_principal)

	def interest_paydown(self):
		return self._paydown(self.cumulative_interest)
