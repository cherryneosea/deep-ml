import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here
    p = np.array(p)
    q = np.array(q)

    if p.size == q.size and len(p) != 0 and len(q) != 0:
        res = np.sum(np.sqrt(np.multiply(p, q)))
        bd = -np.log(res)
        return bd
    else:
        return 0.0