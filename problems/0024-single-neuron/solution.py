import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probs = []
	#neuron output -> vector
	z = np.dot(features, weights) + bias

	#calc the prob of each element using sigmoid
	for i in z:
		sigmoid = np.round(1/ (1 + np.exp(-i)), 4)
		probs.append(sigmoid)

	mse = np.square(np.subtract(probs, labels)).mean()



	return probs, mse