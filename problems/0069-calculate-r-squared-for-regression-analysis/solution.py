
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	
	ssr = np.sum((np.subtract(y_true, y_pred)**2))
	sst = np.sum((np.subtract(y_true, y_true.mean())**2))

	r_square = 1 - (ssr/sst)

	return r_square

