import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	#get the given mode and return mean
	#div by nr of give mods: 

	rows = len(matrix)
	cols = len(matrix[0])
	res = []
	if mode == 'column':
		for i in range(cols):
			avg = 0
			for j in range(rows):
				avg += matrix[j][i]
				#print(avg)

			res.append(avg / rows)
		return res

	else:
		for i in range(rows):
			avg = 0 
			for j in range(cols):
				avg += matrix[i][j]
			res.append(avg / cols)
		return res 
