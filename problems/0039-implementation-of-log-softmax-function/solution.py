import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	#1.calc softmax term
	softs = 0
	for j in range(len(scores)):
		power = scores[j] - max(scores)
		e = np.exp(power)
		softs += e


	log_softmax = []
	for i in range(len(scores)):
		term = scores[i] - max(scores)
		log_softmax.append( term - np.log(softs))

	return log_softmax