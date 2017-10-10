import numpy as np
import scipy.optimize as spopt
import csv
import sys
import random
from hpolib.benchmarks.synthetic_functions import Bohachevsky


X=[]
y=[]

def wrapper(x):
	X.append(x)
	y_ = b.objective_function(x)['function_value']
	y.append(y_)
	return y_


b = Bohachevsky()

info = b.get_meta_information()
bounds = np.array(info['bounds'])


lower =np.array([i[0] for i in bounds])
upper =np.array([i[1] for i in bounds])
initial = np.array([random.randrange(lower[i],upper[i]) for i in range(0,len(bounds))])



print("Lower_Bounds:",lower)
print("Upper Bounds:",upper)
print("Initial point:",initial)


res = spopt.minimize(wrapper, initial, bounds=bounds, method='SLSQP', options = {"ftol":1e-500 ,"maxiter":200})



X = X[:200]
y = y[:200]


fvals = np.array(y)
# Saving into the csv file with a paramater given from the user
with open('/home/numair/Pictures/ScipyOptimizer/ScipyExperiments/Bohachevsky/'+str(sys.argv[1]),'a') as csvfile:
	writer = csv.writer(csvfile, delimiter='\n')
	writer.writerow(fvals)
