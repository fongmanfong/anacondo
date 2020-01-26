import json
import os
import sys
from .context import anacondo

def generate_sample_block():
	with open(os.path.join(sys.path[0], 'test/sample_data.json'), "r") as json_file:
		data = json.load(json_file)

	return anacondo.Blocks(**data['fake_test'])