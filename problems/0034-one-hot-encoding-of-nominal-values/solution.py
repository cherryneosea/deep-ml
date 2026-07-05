import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	#num of unique vals, can be determined from converting
	#input lst to a set, since it has no duplicates
	n = len(set(x))
	res = []

	if n_col is None:
		#loop over elem
		for i in range(len(x)):
			#lst of size as num of unique categoreis
			lst = [0] * n 
			lst[x[i]] = 1.0
			
			res.append(lst)
		return res  

	else:
		for i in range(len(x)):
			lst = [0] * n_col
			lst[x[i]] = 1.0
			res.append(lst)
		return res
	