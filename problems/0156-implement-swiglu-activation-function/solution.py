import numpy as np

def SwiGLU(x: np.ndarray) -> np.ndarray:
    """
    Args:
        x: np.ndarray of shape (batch_size, 2d)
    Returns:
        np.ndarray of shape (batch_size, d)
    """
    # Your code here
    res = np.split(x, 2, axis=-1) #split into 2 equal halfs along features dim
    x1 = res[0]
    x2 = res[1]
    sig = 1 / (1+np.exp(-x2))
    swiglu = x1 * (x2 * sig)
    scores = swiglu
    return np.round(scores, 4)