def parameter_grid_cleaner(block, param_grid):
	return {k: param_grid[k] for k in param_grid.keys() if k in block.__dict__.keys()}
