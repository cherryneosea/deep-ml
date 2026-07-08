def calculate_brightness(img):
	# Write your code here
	#endge cases
	if len(img) == 0:
		return -1
	#check row lenghts for consistency:
	for i in range(len(img)-1):
		if len(img[i]) != len(img[i+1]):
			return -1

	#check for value range 0-255
	summation = 0
	rows = len(img)
	cols = len(img[0])
	for i in range(rows):
		for j in range(cols):
			if 0<= img[i][j] <= 255:
				summation += img[i][j]
			else:
				return -1
	
	return summation / (rows * cols)

