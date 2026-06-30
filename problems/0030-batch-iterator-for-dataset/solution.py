import numpy as np


def batch_iterator(X, y=None, batch_size=64):
    num_samples = len(X)
    batches = []
    for i in range(0, num_samples, batch_size):
        start = i
        end = i + batch_size
        if y is not None:
            batches.append([X[start:end], y[start:end]])
        else:
            batches.append(X[start:end])
    return batches
			
	

