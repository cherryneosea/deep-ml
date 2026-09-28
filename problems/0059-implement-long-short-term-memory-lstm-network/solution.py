import numpy as np

class LSTM:
	def __init__(self, input_size, hidden_size):
		self.input_size = input_size
		self.hidden_size = hidden_size

		# Initialize weights and biases
		self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

		self.bf = np.zeros((hidden_size, 1))
		self.bi = np.zeros((hidden_size, 1))
		self.bc = np.zeros((hidden_size, 1))
		self.bo = np.zeros((hidden_size, 1))

	def forward(self, x, initial_hidden_state, initial_cell_state):
		"""
		Processes a sequence of inputs and returns the hidden states, final hidden state, and final cell state.
		"""
		def sigmoid(x):
			return 1 / (1 + np.exp(-x))

		#init 
		c = initial_cell_state
		h = initial_hidden_state
		outputs = []

		#process input sequence
		for t in range(x.shape[0]):
			xt = x[t].reshape(-1,1)
			#forget gate, concatenate vector
			combined = np.vstack((h, xt))  # shape: (hidden_size + input_size, 1)
			ft = sigmoid(self.Wf @ combined + self.bf)
			#input gate
			it = sigmoid(self.Wi @ combined + self.bi)
			#candidate cell state => creates a vector
			candidate_ct = np.tanh(self.Wc @ combined + self.bc)

			#update cell state 
			ct = np.multiply(ft, c) + np.multiply(it, candidate_ct)

			#outputgate 
			ot = sigmoid(self.Wo @ combined + self.bo)
			ht = np.multiply(ot, np.tanh(ct))
			outputs.append(ht)
			h, c = ht, ct

		return np.array(outputs), h, c

