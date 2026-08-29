import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	matrix = dense_matrix
	vals = []
	cols_idx = []
	row_ptrs = [0]

	

	for i in range(len(matrix)):
		for j in range(len(matrix)):
			#store each none zero elem
			if matrix[i][j] != 0:
				vals.append(matrix[i][j])
				cols_idx.append(j)
		#end of each row we take the nums of vals found
		row_ptrs.append(len(vals))
			

	return (vals, cols_idx, row_ptrs)
