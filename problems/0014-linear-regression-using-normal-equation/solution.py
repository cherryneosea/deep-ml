import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	t = np.transpose(X)
	prod = np.dot(t, X)
	inverse = np.linalg.inv(prod)
	theta = np.dot(np.dot(inverse, t), y)
	return theta