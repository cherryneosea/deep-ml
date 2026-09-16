import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	#check invertibility of T en
	T = np.array(T)
	S = np.array(S)
	A = np.array(A)

	det_T = np.linalg.det(T)
	det_S = np.linalg.det(S)


	if det_S != 0 and det_T != 0:
		#t invers
		inverse_T = np.linalg.inv(T)
		res = inverse_T @ A @ S
		return res.tolist()
	else: 
		return -1
	