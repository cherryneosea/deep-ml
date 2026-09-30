import numpy as np

def softmax(values):
    values = np.array(values, dtype=float)
    shifted = values - np.max(values)  # for numerical stability
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)

def pattern_weaver(n, crystal_values, dimension):
	# Your code here
	final = []
	for i in range(n):
		#get current element and calc its nrelation to every other in that row 
		value_i = []
		for j in range(n):
			#take product
			value_i.append((crystal_values[i] * crystal_values[j]) / (dimension **(1/2)))

		#now we have attention score for elemi aka after processing the full row i
		soft_scores = softmax(np.array(value_i))

			#final output
		output = np.sum(soft_scores * crystal_values)
		final.append(output)



	return np.round(final,3)