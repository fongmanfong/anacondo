from sklearn.model_selection import ParameterGrid
from .blocks import Blocks
import numpy as np
from copy import deepcopy

class ScenarioAnalyzer(object):
    
    def __init__(self, block_object):
            # self.__dict__.update(block_object.__dict__)
            self.block = block_object
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

    @staticmethod
    def _parameter_grid(param_grid):
        return ParameterGrid(param_grid)


    PARAM_INCREMENT_DICT = {
            'purchase_price': 10000,
            'interest_rate': 0.005,
            'rental_income': 100
    }

    @staticmethod
    def _calculate_break_even_year(time_series):
        return len(time_series) - sum(time_series >= 0)

    def compute_financial_metric_break_even(self, param_grid, increment_param_grid=None):
        
        # check param grid fits what design [min max value]
        # check if param grid values are correct

        param_grid_exploded = {}
        param_results = []
        sim_block_unit = deepcopy(self.block)
        increment_grid = {}

        if increment_param_grid != None:
            increment_grid = increment_param_grid
        else:
            increment_grid = self.PARAM_INCREMENT_DICT

        for key, value in param_grid.items():
            param_grid_exploded[key] = np.round(np.arange(value[0], value[1], increment_grid[key]), decimals=4)

        for params in self._parameter_grid(param_grid_exploded):
            sim_block_unit.__dict__.update(params)
            for i in ['coc', 'roi', 'roe']:
                params[i] = self._calculate_break_even_year(self.financial_metric_selector(sim_block_unit, i)())
            param_results.append(params)

        return param_results




    def compute_scenarios(self, metric, param_grid):
        param_results = []
        sim_block_unit = deepcopy(self.block)
        
        for params in self._parameter_grid(param_grid):
            sim_block_unit.__dict__.update(params)
            params[metric] = self.financial_metric_selector(sim_block_unit, metric)()
            param_results.append(params)
        
        return param_results
            # param_results[param_grid] = sim_block_unit.cash_on_cash_return()
            
