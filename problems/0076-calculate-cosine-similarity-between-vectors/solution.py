import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	nom = 0
	denom = 0

	if (v1.size != 0 and v2.size != 0 and 
		v1.size == v2.size):
		nom = np.dot(v1, v2)
		denom = np.sqrt(np.sum(v1**2)) * np.sqrt(np.sum(v2**2))

	if denom != 0:
		cos_sim = nom / denom
		return cos_sim
