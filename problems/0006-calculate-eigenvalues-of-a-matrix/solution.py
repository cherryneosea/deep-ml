def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	

	#flatten matrix
	elems = []
	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			elems.append(matrix[x][y])

	#calc ad en bc
	ad = elems[0] * elems[3]
	bc = elems[1] * elems[2]
	
	#solve quadratic equation
	a = 1
	b = -(elems[0] + elems[3]) #negated trace
	c = ad - bc #determinant 

	#calc discriminant
	discr = (b**2) - 4 * c 

	d = (discr) ** 0.5 #correct exponent grouping


	if d == 0:
		eigenvalues = [-b / (2* a), -b / (2* a)]

	else:
		# Corrected division precedence
        e1 = (-b + d) / (2 * a)
        e2 = (-b - d) / (2 * a)
        eigenvalues = [e1, e2]

	#sort from highest to lowest
	eigenvalues.sort(reverse=True)

	return eigenvalues





