import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	# Your code here
	#padding input matrix
	padded_input = np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0)

	#init output matrix with zeros
	#adding the padded dims 
	# 2 bcs you add paddings top, bottom, left, right
	padded_h = input_height + 2 * padding
	padded_w = input_width + 2 * padding

	output_h = ((padded_h - kernel_height) // stride) + 1
	output_w = ((padded_w - kernel_width) // stride) + 1

	output_matrix = np.zeros((output_h, output_w))

	#performing convulotion
	for row in range(output_h):
		for col in range(output_w):
			#extract sub-matrix from padded input to apply kernel  col en row
			sub_region = padded_input[row*stride : row*stride + kernel_height, col*stride : col*stride + kernel_width]
			#elem wise multipliplication input X kernel
			prod = kernel * sub_region
			som = np.sum(prod)
			#store the single value to output
			output_matrix[row, col] = som

    
	return output_matrix
