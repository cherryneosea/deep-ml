def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	

	#notes= each elem of vector x each col -> vector

	#define ranges of matrices
	n_rows = len(a)
	m_cols = len(a[0])
	vec_len = len(b)
	res = []

	if m_cols != vec_len:
		return -1
	else:
		#loop over rows and cols -> multiply each elem on idx ij with elem on idx 0j sum per row
		for i in range(len(a)):
			sum_row = 0
			for j in range(len(a[0])):
				sum_row += a[i][j] * b[j]
			#append once per row
			res.append(sum_row)
	return res
				