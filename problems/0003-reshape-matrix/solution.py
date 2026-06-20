import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	rows, cols = new_shape
	#flatten lst
	lst = sum(a, [])
	if rows * cols != len(lst):
		return []
	#combine in pairs
	else:

		b = []
		for i in range(rows):
			e = []
			for j in range(cols):
				#comb to pairs per row table idx to single idx
				e.append(lst[i*cols + j])
			b.append(e)


	return b