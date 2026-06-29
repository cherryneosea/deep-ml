import math
import numpy as np

def sigmoid(z: float) -> float:
	#Your code here
	expression = 1/(1 + np.exp(-z))
	
	if z == 0:
		return 0.5
	else:
		return expression
