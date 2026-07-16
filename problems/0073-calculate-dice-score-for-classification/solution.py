
import numpy as np


def dice_score(y_true, y_pred):
    tp = np.sum(y_true * y_pred)
    denom = np.sum(y_true) + np.sum(y_pred)
    
    if denom == 0:
        return 0.0
    
    return round(2 * tp / denom, 3)