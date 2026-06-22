import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here

    # Standardization
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized = np.round((data - mean) / std, 4)
    
    # Min-Max Normalization
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    minmax = np.round((data - min_val) / (max_val - min_val), 4)
    
    return standardized.tolist(), minmax.tolist()