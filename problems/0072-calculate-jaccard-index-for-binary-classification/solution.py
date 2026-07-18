
import numpy as np


def jaccard_index(y_true, y_pred):
    intersection = np.sum(y_true & y_pred)
    union = np.sum(y_true | y_pred)
    
    if union == 0:
        return 0.0
    
    result = intersection / union
    return round(result, 3)
