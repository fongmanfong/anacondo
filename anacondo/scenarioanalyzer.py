from sklearn.model_selection import ParameterGrid
from .blocks import Blocks
from .utils import parameter_grid_cleaner
import numpy as np
from copy import deepcopy

class ScenarioAnalyzer(object):
   
    """
    This class creates a ScenarioAnalyzer object that allows different scenarios to be simulated for a block object


    Parameters
    -----------
    block_object: block
        The block object (real estate property) that is of interest   
    """

    def __init__(self, block_object):
            self.block = block_object
            self.cash_on_cash_return = block_object.cash_on_cash_return
            self.return_on_equity = block_object.return_on_equity
            self.return_on_investment = block_object.return_on_investment
            self.annualized_return = block_object.annualized_return

    PARAM_INCREMENT_DICT = {
            'purchase_price': 10000,
            'interest_rate': 0.005,
            'rental_income': 100
    }

    @staticmethod
    def financial_metric_selector(block, metric):
    	
    	financial_metric_select = {
    		'coc': block.cash_on_cash_return,
    		'roe': block.return_on_equity,
    		'roi': block.return_on_investment,
    		'apy': block.annualized_return
    	}

    	try:
    		return financial_metric_select[metric]
    	except:
    		print ('Valid financial metric parameters: coc, roe, roi, apy')

    @staticmethod
    def _parameter_grid(param_grid):
        return ParameterGrid(param_grid)

    @staticmethod
    def _calculate_break_even_year(time_series):
        return len(time_series) - sum(time_series >= 0)

    def compute_break_even(self, param_grid, increment_param_grid=None):
        
        # check param grid fits what design [min max value]
        # check if param grid values are correct
        param_grid = parameter_grid_cleaner(self.block, param_grid)
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

    def compute_scenarios_set(self, metric, param_grid):

        param_grid = parameter_grid_cleaner(self.block, param_grid)
        param_results = []
        sim_block_unit = deepcopy(self.block)
        
        for params in self._parameter_grid(param_grid):
            sim_block_unit.__dict__.update(params)
            params[metric] = self.financial_metric_selector(sim_block_unit, metric)()
            param_results.append(params)
        
        return param_results

    def compute_scenarios_mc(self, metric, param_grid, year=5, sample_size=300):

        # Compute return of different scenarios using monte carlo simulation. Each parameter is a vector of samples from a assumed distribution
        # Vectors must be equal length e.g. 'interest_rate': np.random.normal(loc=0.035, scale=0.005, size=100)

        # check to make sure length of simulation are all the same
        param_grid = parameter_grid_cleaner(self.block, param_grid)

        sampled_param_grid = {}
        metric_return = []
        sim_block_unit = deepcopy(self.block)

        for i in range(0, sample_size):
            for key, value in param_grid.items():
                sampled_param_grid[key] = value[i] # sample from distribution and create new parameter grid

            sim_block_unit.__dict__.update(sampled_param_grid)
            metric_return.append(self.financial_metric_selector(sim_block_unit, metric)())

        if year >= 0:
            return np.vstack(metric_return)[:, year]
        else:
            # implement after
            pass 



            
