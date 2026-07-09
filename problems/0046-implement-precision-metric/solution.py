import numpy as np
def precision(y_true, y_pred):
	# Your code here
	#loop over 2 funcs in parallel
	tp = 0
	fp = 0
	for i, j in zip(y_true, y_pred):
		if i == 1 and j == 1:
			tp += 1
			print(tp)
		if i == 0 and j == 1:
			fp += 1
		else:
			 0 

	return tp / (tp+fp)
