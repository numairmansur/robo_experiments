import math
import random
from moe.easy_interface.experiment import Experiment
from moe.easy_interface.simple_endpoint import gp_next_points
from moe.optimal_learning.python.data_containers import SamplePoint
import numpy as np
import csv
import sys
from hpolib.benchmarks.synthetic_functions import Branin


X = []
y = []

def wrapper(x,b):
    X.append(x)
    y_ = b.objective_function(x)['function_value']
    y.append(y_)
    return y_



def run_example(num_points_to_sample=200, verbose=False, **kwargs):
	b = Branin()
	bounds = b.get_meta_information()['bounds']
	dimensions = len(bounds)
	lower =np.array([i[0] for i in bounds])
	upper =np.array([i[1] for i in bounds])
	start_point = (upper-lower)/2
	exp = Experiment([lower,upper])
	exp.historical_data.append_sample_points([
        SamplePoint(start_point, wrapper(start_point,b), 0.6)])
	for _ in range(num_points_to_sample):
		next_point_to_sample = gp_next_points(exp, **kwargs)[0]
		value_of_next_point = wrapper(next_point_to_sample,b)
		if verbose:
			print "Sampled f({0:s}) = {1:.18E}".format(str(next_point_to_sample), value_of_next_point)
		exp.historical_data.append_sample_points([SamplePoint(next_point_to_sample, value_of_next_point, 0.6)])



if __name__ == '__main__':
	print("Running for " + str(sys.argv[1]) + "...")
	run_example()
	X = X[:200] 
	y = y[:200]
	fvals = np.array(y)
	with open('/home/numair/Pictures/MOE/moeExperiments/Branin/'+ str(sys.argv[1]), 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter='\n')
		writer.writerow(fvals)