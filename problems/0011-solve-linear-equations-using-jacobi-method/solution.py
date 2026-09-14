import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	

	#start with x=0
	x = np.zeros(len(b))

	#iterate max n times
	for iteration in range(n):
		#iterate over the product of the matrix
		new_x = np.zeros(len(b))

		for i in range(A.shape[0]):
			total = 0
			for j in range(A.shape[1]):
				if i != j:
					total += A[i][j] * x[j]

			new_x[i] = (b[i] - total) / (A[i][i])
		x = new_x

		

	return x 
