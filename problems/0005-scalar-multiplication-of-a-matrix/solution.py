def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	

	rows = len(matrix)
	cols = len(matrix[0])

	for x in range(rows):
		for y in range(cols):
			matrix[x][y] *= scalar
	return matrix
