
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	total = len(y)
	#convert y to np array
	y = np.array(y)
	unique = np.unique(y)
	probs = 0
	for i in unique:
		#count prob for each unique
		p = np.sum( y == i) / total
		probs += p**2
			

	return round(1-probs,3)