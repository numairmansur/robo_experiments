import cma
import numpy as np
import csv
import sys
from hpolib.benchmarks.synthetic_functions import Bohachevsky


X=[]
y=[]

def wrapper(x):
	X.append(x)
	y_ = b.objective_function(x)['function_value']
	y.append(y_)
	return y_


b = Bohachevsky()
# Dimension and bounds of the function
bounds = b.get_meta_information()['bounds']
dimensions = len(bounds)
lower =np.array([i[0] for i in bounds])
upper =np.array([i[1] for i in bounds])

start_point = (upper-lower)/2

# Evolution Strategy
es = cma.CMAEvolutionStrategy(start_point, 0.6, {'bounds': [lower,upper], "maxfevals":200})
logger = cma.CMADataLogger().register(es)

es.optimize(wrapper,200)

X = X[:200] 
y = y[:200]


fvals = np.array(y)
# Saving into the csv file with a paramater given from the user
with open('/home/numair/Pictures/CMA-RUNS/cmaExperiments/Bohachevsky/'+str(sys.argv[1]),'a') as csvfile:
	writer = csv.writer(csvfile, delimiter='\n')
	writer.writerow(fvals)
