import numpy as np

# years should be Print eventually probably

class Mortgage(object):

	def __init__(self, purchase_price, interest_rate, down_payment_pct, loan_term, years=30):
		self.interest_rate = interest_rate
		self.down_payment_pct = down_payment_pct
		self.loan_term = loan_term
		self.purchase_price = purchase_price
		self.years=years

	def _generate_years(self):
		return range(1,self.years+1)

	def loan_amount(self):
		return self.purchase_price * (1 - self.down_payment_pct)

	def monthly_payments(self):
		return -np.pmt(self.interest_rate / 12.0, self.loan_term * 12, self.loan_amount())

	def annual_payment(self):
		return self.monthly_payments()*12

	def payment_over_term(self):
		pass

	def _cumulative_principal(self, start, end, rate, nper, pv):
		cp = 0
		for i in range(start,end+1):
			cp = cp + (-np.ppmt(rate / 12, i, nper*12, pv))
		return cp

	def mortgage_balance(self):
		return np.array([round(np.fv(self.interest_rate / 12.0, i*12, self.monthly_payments(), -self.loan_amount()), 2) for i in self._generate_years()])

	def principal_paydown(self):
		return np.array([self._cumulative_principal(i*12-11, i*12, self.interest_rate, self.loan_term, self.loan_amount()) for i in self._generate_years()])