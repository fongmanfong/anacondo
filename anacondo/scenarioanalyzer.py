from sklearn.model_selection import ParameterGrid
from .blocks import Blocks
import numpy as np

class ScenarioAnalyzer(object):
    
    def __init__(self, block_object, param_grid):
            self.__dict__.update(block_object.__dict__)
            self.block = block_object
            self.param_grid = param_grid
            self.grid = ParameterGrid(self.param_grid)
            self.cash_on_cash_return = block_object.cash_on_cash_return
            self.return_on_equity = block_object.return_on_equity
            self.return_on_investment = block_object.return_on_investment
            self.annualized_return = block_object.annualized_return
       
    def financial_metric_selector(self, block, metric):
    	
    	financial_metric_select = {
    		'coc': block.cash_on_cash_return,
    		'roe': block.return_on_equity,
    		'roi': block.return_on_investment,
    		'apy': block.annualized_return
    	}

    	try:
    		return financial_metric_select[metric]
    	except:
    		print ('input value incorrect')

#     def simulate_break_even(self, metric, parameter):
# 
#     	sim_block_unit = self.block
# 
#     	parameter_select = {
#     		'purchase_price': self.purchase_price,
#     		'interest_rate': self.interest_rate
#     	}
# 
#     	default_increments_select = {
#     		'purchase_price': 1000,
#     		'interest_rate': 0.002
#     	}
# 
#     	default_start_select = {
#     		'purchase_price': 100000,
#     		'interest_rate': 0.01
#     	}
# 
#     	try:
#     		financial_function = self.financial_metric_selector(sim_block_unit, metric)
#     		increments = default_increments_select[parameter]
#     		start = default_start_select[parameter]
#     		original_parameter_value = parameter_select[parameter]
#     	except:
#     		print ('input value incorrect 2')
# 
#     	year_counter = 30 # change
#     	break_even_dict = {} # stores break_even_value: year
# 
#     	import pdb; pdb.set_trace()
#     	while year_counter !=0:
#     		print (break_even_dict)
#     		sim_block_unit.update(**{parameter: start})
#     		if np.sum(financial_function() > 0) < year_counter:
#     			break_even_dict[np.round(start, 4)] = abs(year_counter - 30) + 1
#     			year_counter -= 1
#     		start += increments
#     	
#     	return break_even_dict

    def compute_scenarios(self, metric):
        param_results = []
        sim_block_unit = self.block
        
        for params in self.grid:
            sim_block_unit.__dict__.update(params)
            params[metric] = self.financial_metric_selector(self, metric)()
            param_results.append(params)
        
        return param_results
            # param_results[param_grid] = sim_block_unit.cash_on_cash_return()
            
