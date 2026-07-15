import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	#calc predicted vals 
	y_pred = np.dot(X, w)
	t1 = np.sum(np.subtract(y_true, y_pred)**2) / X.shape[0]
	t2 = alpha * np.sum(w**2)

	return t1+t2
