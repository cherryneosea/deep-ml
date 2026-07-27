import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	# Your code here
	rows = x.shape[0]
	cols = x.shape[1]
	channel = x.shape[2]
	total = rows * cols
	res = []
	#add all elements od same col, diff rows
	for c in range(channel):
		som = 0
		for i in range(rows):
			for j in range(cols):
				#access
				som += x[i, j, c]
		res.append(som/total)

	#convert to np
	return np.array(res)