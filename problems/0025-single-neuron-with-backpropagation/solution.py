import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	
	#initilize vars
	updated_w = initial_weights.copy()
    updated_bias = initial_bias
    mse_vals = []
    num_samples = labels.shape[0]

	#in each epoch 
	for epoch in range(epochs):
		#1.forward pass
		#calculate the weighted sum z 
		z = np.dot(features, updated_w) + updated_bias
		#pass to activation function
		sig_z = 1 / (1 + np.exp(-z))
		#calculate the loss based on the predicted label
		mse = np.mean((np.subtract(sig_z, labels)) ** 2) 
		#add it to mse 
		mse_vals.append(float(mse))

		#2.backward pass to calculate gradient
		#take partial derv of mse with respect to w, bias 
		#prediction errors
		errors = np.subtract(sig_z, labels)
		sig_deriv = np.multiply(sig_z, np.subtract(1, sig_z))
		chain_rule_deriv = 2 * errors * sig_deriv

		#weighted gradient averaged
		X_transposed = np.transpose(features)
		w_grad = (np.dot(X_transposed, chain_rule_deriv)) / num_samples

		#bias gradient averaged
		bias_grad = (np.sum(chain_rule_deriv, axis=0)) / num_samples

		#pars update 
		updated_w = updated_w - learning_rate * w_grad
		updated_bias = updated_bias - learning_rate * bias_grad
	

	return updated_w, updated_bias, mse_vals









