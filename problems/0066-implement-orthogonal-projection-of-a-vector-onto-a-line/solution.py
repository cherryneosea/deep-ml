
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""

	nom = []
	denom = []

	for i, j in zip(v, L):
		nom.append( i * (j**2))

	for i in range(len(L)):
		denom.append(L[i] * L[i])

	fraction = []
	for i, j in zip(nom, denom):
		if j != 0:
			fraction.append(i/ j)
		else:
			fraction.append(0)
	return fraction 

	
