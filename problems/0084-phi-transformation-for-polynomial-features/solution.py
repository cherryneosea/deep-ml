import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	# Your code here
	#for each feature make a lst and transform
	res = []
	for i in range(len(data)):
		row = []
		for d in range(degree + 1):
			e = data[i] ** d 
			row.append(e)
		res.append(row)
	return res



