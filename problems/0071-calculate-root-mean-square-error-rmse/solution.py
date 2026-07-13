
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	rmse = np.sqrt(np.sum(np.subtract(y_true, y_pred)**2)/y_pred.size)
	return round(rmse,3)
