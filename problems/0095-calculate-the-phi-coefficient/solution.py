def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	x00 = 0
	x01 = 0
	x10 = 0
	x11 = 0
	#loop through both
	for i, j in zip(x,y):

		if i == 0 and j == 0:
			x00 += 1

		elif i == 0 and j == 1:
			x01 += 1

		elif i == 1 and j == 0:
			x10 += 1

		else:
			x11 += 1

	nom = (x00 * x11) - (x01 * x10)
	denom = ((x00+x01)*(x10+x11)*(x00+x10)*(x01+x11))**(1/2)

	if denom != 0:
		val = nom / denom
	else:
		val = 0 
		
	return round(val,4)

