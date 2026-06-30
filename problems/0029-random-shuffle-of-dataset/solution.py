import numpy as np
import math

def shuffle_data(X, y, seed=None):
	# Your code here
	#set seed for reproducibilty 
	np.random.seed(seed)
	
	#generate an array of idx corr to num of samples
	"""idx_arr = []
	for i in range(len(X)):
		idx_arr.append(i)"""
	#alt using np
	idx = np.arange(len(X)) #creat idx arr

	#shuffle those idx in place
	np.random.shuffle(idx)
	
	#reorder dataset such that the random xi corr to true yi-label
	return X[idx], y[idx]

