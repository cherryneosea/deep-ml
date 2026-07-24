def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	#count unique colors in set
	k = len(set(apples))

	def elem_counter(c, lst):
		#count how many elements of given color
		cnt = 0
		for i in range(len(lst)):
			if lst[i] == c:
				cnt += 1
		return cnt 

	#calc prop color per color
	pi = 0
	gini = 0
	for color in range(k):
		#how many apples in i color
		pi = elem_counter(color , apples) / len(apples)
		gini += pi ** 2

	return 1 -gini 




