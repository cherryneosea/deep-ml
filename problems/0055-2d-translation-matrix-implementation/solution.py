import numpy as np
def translate_object(points, tx, ty):
	#to move x,y in matrix by tx en ty in x and y direction, but they still represent og points 
	# Step 1: Convert to homogeneous coordinates by stacking a column of 1s
		points = np.array(points)
		ones = np.ones((points.shape[0], 1))
		homogeneous_points = np.hstack([points, ones])
		
		# Step 2: Build the translation matrix
		translation_matrix = np.array([
			[1, 0, tx],
			[0, 1, ty],
			[0, 0, 1]
		])
		
		# Step 3: Apply the transformation (note the transpose for correct shape)
		translated_homogeneous = homogeneous_points @ translation_matrix.T
		
		# Step 4: Drop the homogeneous coordinate (the last column)
		translated_points = translated_homogeneous[:, :2]
		
		return translated_points.tolist()
