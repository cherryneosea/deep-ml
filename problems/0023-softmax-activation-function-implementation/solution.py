import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    #calc the som of all scores

    sum_z = 0
    max_z = max(scores)
    res = []

    for i in range(len(scores)):
        e = scores[i]
        power = e - max_z
        sum_z += np.exp(power)

    #calc the softmax score
    for i in range(len(scores)):
        e = scores[i]
        power = e - max_z
        term = np.round(np.exp(power) / sum_z, 4)
        res.append(term)

    return res 
