import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	beta_sqrt = beta ** 2
	
	# Calculate counts
	true_positives = np.sum((y_pred == 1) & (y_true== 1))
	false_positives = np.sum((y_pred == 1) & (y_true == 0))
	false_negatives = np.sum((y_pred == 0) & (y_true == 1))

	# Compute metrics
	precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0

	recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

	f_score = np.round( ((1 + beta_sqrt) *(precision * recall)) / ((beta_sqrt * precision) + recall), 3)

	return f_score
