import pandas as pd
import numpy as np
import json
from .mortgage import Mortgage

class Blocks(Mortgage):

	"""
    This class creates a Block object that represents a real estate property. This class inherits
    from Mortgage as mortgage information is part of property assessment.

    Parameters
    -----------
    rental_income: float
    	Monthly rental income from property
    vacany: TBD, optional
    	Vacancy rate or vacancy days? TBD
    maintenance_reserve: TBD, optional (default=0)
    	Reserve amount paid. TBD
    management_fee: TBD, optional
    	Property management fee. Should this be dollar or percentage?
    monthly_property_tax: float, optional (default=0)
    	Monthly property tax in dollar amount
    monthly_insurance: float, optional (default=0)
    	Monthly insurance in dollar amount
    monthly_utility: float, optional (default=0)
    	Monthly utility cost in dollar amount
    rental_income_increase: float, optional (default=0)
    	Yearly rental income increase in percentage. Values between 0 and 1
    property_tax_increase: float, optional (default=0)
    	Yearly property tax increase in percetange. Values between 0 and 1
    closing_cost_buy: float, optional (default=0)
    	Dollar amount required upon closing property
    closing_cost_sell; float, optional (default=0)
    	Dollar amount required upon sellign property
   
    """


# don't need property_value. put in property value growth?
# plotting is quite useless since its mostly linear. Just print table is important

	def __init__(self, property_value, purchase_price, interest_rate, down_payment_pct, loan_term, rental_income, 
				 vacancy=0, maintenance_reserve=0, management_fee=0, monthly_property_tax=0, monthly_insurance=0,
				 monthly_utility=0, rental_income_increase=0, property_tax_increase=0,
				 closing_cost_buy=0, closing_cost_sell=0, years=30):

		super(Blocks, self).__init__(purchase_price, interest_rate, down_payment_pct, loan_term, years)

		self.property_value = property_value
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

		# Print formatting --> move to Print class after?
		self.decimals = 4

	def _project_metric_yoy_growth(self, base, growth):
		return np.array([self._yearly_increase(base, growth, i) for i in self._generate_years()])

	def _project_metric_constant(self, metric, period):
		return np.full(max(self._generate_years()), metric*period)

	def _yearly_increase(self, base, yoy_pct_incr, years):
		return round(12*base*(1+yoy_pct_incr/100.0) ** ((years * 12 - 12 ) / 12.0), 2)

	def down_payment_amount(self):
		return self.purchase_price * self.down_payment_pct

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
		return self.annual_cash_flow() / 12.0

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

	def equity_wealth(self):
		return self.property_value - self.mortgage_balance()

	def plus_sales_proceeds_if_final_year(self):
		return np.round(self.annual_cash_flow() + self.equity_wealth() - self.property_value*self.closing_cost_sell, self.decimals)

	def effective_future_value(self):
		return self.plus_sales_proceeds_if_final_year() + self.accumulated_cash_flow() + self.annual_cash_flow()

	# Financial Performance

	def capitalization_rate(self): 
		return np.round(self.net_operating_income() / self.property_value, self.decimals)

	def cash_on_cash_return(self):
		return np.round(self.annual_cash_flow() / self.total_cash_required(), self.decimals)

	def return_on_equity(self):
		return np.round(self.effective_net_cash_flow() / self.equity_wealth(), self.decimals)

	def annualized_return(self):
		annualized_return = self.effective_future_value() / self.total_cash_required()
		for i in range(0,len(annualized_return)):
			annualized_return[i] = annualized_return[i]**(1/(i+1))-1
		return annualized_return

	def return_on_investment(self):

		# accumulated cash flow up to but no including current period
		shifted_accumulate_cash_flow = np.delete(np.insert(self.accumulated_cash_flow(), 0, 0), -1)
		return np.round((self.plus_sales_proceeds_if_final_year() + shifted_accumulate_cash_flow - self.total_cash_required()) / self.total_cash_required(), self.decimals)

	# Print (move to seperate class)
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

	def simulate_break_even(self, financial_metric, parameter, default_increments=True, start=1, end=None):

		financial_metric_select = {
			'coc': self.cash_on_cash_return,
			'roe': self.return_on_equity,
			'roi': self.return_on_investment,
			'apy': self.annualized_return
		}

		parameter_select = {
			'purchase_price': self.purchase_price,
			'interest_rate': self.interest_rate
		}

		try:
			financial_function = financial_metric_select[financial_metric]
			original_parameter_value = parameter_select[parameter]
		except:
			print ('input value incorrect')

		year_counter = self.years
		price_dict = {}

		while year_counter !=0:
			self.update(**{parameter: start})
			if np.sum(financial_function() > 0) < year_counter:
				price_dict[start] = abs(year_counter - self.years)
				year_counter -= 1
			start += 1000

		parameter_select[parameter] = original_parameter_value
		return price_dict

	def update(self, **kwargs):
		self.__dict__.update((k, kwargs[k]) for k in set(kwargs).intersection(self.__dict__))

	def save(self, property_name):

		self_param_dict = self.__dict__.copy()
		del self_param_dict['decimals'], self_param_dict['years']

		with open('anacondo/history.json', 'w') as outfile:
			json.dump({property_name: self_param_dict}, outfile)

	# have the ability to print financial statement?
