import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	#start by comparing pred, and storing them
	preds = []
	for i, j in zip(y_true, y_pred):
		#using zip to pair lsts togther and access elems directly
		preds.append(i==j)
	return sum(preds)/len(y_pred)
		