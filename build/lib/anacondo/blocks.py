import pandas as pd
import numpy as np

class Blocks(object):

	def __init__(self, property_value, purchase_price, interest_rate, down_payment_pct, loan_term, rental_income, 
				 vacancy=0, maintenance_reserve=0, management_fee=0, monthly_property_tax=0, monthly_insurance=0,
				 monthly_utility=0, rental_income_increase=0, property_tax_increase=0,
				 closing_cost_buy=0, closing_cost_sell=0, years=30):

		self.property_value = property_value
		self.purchase_price = purchase_price
		self.interest_rate = interest_rate
		self.down_payment_pct = down_payment_pct
		self.loan_term = loan_term
		self.rental_income = rental_income
		self.vacancy = vacancy
		self.maintenance_reserve = maintenance_reserve
		self.management_fee = management_fee
		self.monthly_property_tax = monthly_property_tax
		self.monthly_insurance = monthly_insurance
		self.monthly_utility = monthly_utility
		self.rental_income_increase = rental_income_increase
		self.property_tax_increase = property_tax_increase
		self.closing_cost_buy = closing_cost_buy
		self.closing_cost_sell = closing_cost_sell
		self.years = years

	def _project_metric_yoy_growth(self, base, growth):
		return np.array([self._yearly_increase(base, growth, i) for i in self._generate_years()])

	def _project_metric_constant(self, metric, period):
		return np.full(max(self._generate_years()), metric*period)

	def _yearly_increase(self, base, yoy_pct_incr, years):
		return round(12*base*(1+yoy_pct_incr/100) ** ((years * 12 - 12 ) / 12), 2)

	def _generate_years(self):
		return range(1,self.years)

	def _cumulative_principal(self, start, end, rate, nper, pv):
		cp = 0
		for i in range(start,end+1):
			cp = cp + (-np.ppmt(rate / 12, i, nper*12, pv))
		return cp

    # General 

	def down_payment_amount(self):
		return self.purchase_price * self.down_payment_pct

	def loan_amount(self):
		return self.purchase_price * (1 - self.down_payment_pct)

	def annual_payment(self):
		return self.monthly_payments()*12

	def monthly_payments(self):
		return -np.pmt(self.interest_rate / 12, self.loan_term * 12, self.loan_amount())

	def total_cash_required(self):
		return self.down_payment_amount() + self.closing_cost_buy*self.loan_amount()

	# Cash Flow

	def property_management_amt(self):
		return self.gross_scheduled_income() * self.management_fee

	def insurance(self): # function to change insurance payment over time?
		return self._project_metric_constant(self.monthly_insurance, 12)

	def utility(self):
		return self._project_metric_constant(self.monthly_utility, 12)

	def gross_scheduled_income(self):
		return self._project_metric_yoy_growth(self.rental_income, self.rental_income_increase)
	
	def property_tax(self):
		return self._project_metric_yoy_growth(self.monthly_property_tax, self.property_tax_increase)

	def annual_cash_flow(self):
		return self.net_operating_income() - self.annual_payment()

	def monthly_cash_flow(self):
		return self.annual_cash_flow() / 12

	def total_operating_income(self):
		return self.gross_scheduled_income() + 0

	def net_operating_income(self):
		return self.total_operating_income() - self.total_operating_expense()	

	def total_operating_expense(self):
		return self.property_tax() + self.insurance() + self.utility() + self.property_management_amt()

	def effective_net_cash_flow(self):
		return self.annual_cash_flow() + self.principal_paydown()

	def accumulated_cash_flow(self):
		return np.cumsum(self.annual_cash_flow())

	# Equity Accumulation

	def equity_at_purchase(self): # DOUBLE CHECK
		return self.property_value - self.purchase_price + self.down_payment_amt

	def mortgage_balance(self):
		return np.array([round(np.fv(self.interest_rate / 12, i*12, self.monthly_payments(), -self.loan_amount()), 2) for i in self._generate_years()])

	def principal_paydown(self):
		return np.array([self._cumulative_principal(i*12-11, i*12, self.interest_rate, self.loan_term, self.loan_amount()) for i in self._generate_years()])

	def equity_wealth(self):
		return self.property_value - self.mortgage_balance()

	def plus_sales_proceeds_if_final_year(self):
		return self.annual_cash_flow() + self.equity_wealth() - self.property_value*self.closing_cost_sell

	def effective_future_value(self):
		return self.plus_sales_proceeds_if_final_year() + self.accumulated_cash_flow() + self.annual_cash_flow()

	# Financial Performance

	def capitalization_rate(self): 
		return self.net_operating_income() / self.property_value 

	def cash_on_cash_return(self):
		return np.round((self.annual_cash_flow() / self.total_cash_required())*100, 2)

	def return_on_equity(self):
		return self.effective_net_cash_flow() / self.equity_wealth()

	def annualized_return(self):
		annualized_return = self.effective_future_value() / self.total_cash_required()
		for i in range(0,len(annualized_return)):
			annualized_return[i] = annualized_return[i]**(1/(i+1))-1
		return annualized_return

	def return_on_investment(self):
		return (self.plus_sales_proceeds_if_final_year() / self.total_cash_required()) / self.total_cash_required()

	def print_period_sampler(self):
		return list(range(1,11)) + [10, 20, 30]

	def print_financial_performance(self, full_period=False):
		financial_performance_df = pd.DataFrame({
			'Year': [i for i in self._generate_years()],
			'Cash on Cash COC': self.cash_on_cash_return(),
			'Return on Equity ROE': self.return_on_equity(),
			'Annualized Return APY': self.annualized_return(),
			'Return On Investment': self.return_on_investment()
		})

		return financial_performance_df.set_index('Year').T

	# have the ability to print financial statement?
