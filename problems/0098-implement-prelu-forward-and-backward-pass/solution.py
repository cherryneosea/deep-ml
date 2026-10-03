import numpy as np

def prelu_forward(x: np.ndarray, alpha: float = 0.25) -> np.ndarray:
    """
    Implements the forward pass of PReLU.
    Args:
        x: Input array of any shape
        alpha: Slope parameter for negative values (default: 0.25)
    Returns:
        np.ndarray: PReLU activation output, same shape as x
    """
    return np.where(x > 0, x, alpha * x)


def prelu_backward(x: np.ndarray, alpha: float, grad_output: np.ndarray) -> tuple[np.ndarray, float]:
    """
    Implements the backward pass of PReLU, computing gradients for both x and alpha.
    Args:
        x: Original input from forward pass
        alpha: Slope parameter used in forward pass
        grad_output: Upstream gradient, same shape as x
    Returns:
        grad_x: Gradient w.r.t. input x, same shape as x
        grad_alpha: Gradient w.r.t. alpha (scalar, summed over all elements)
    """
    # Your code here
    mask = x > 0 #boolean array matchin piecewise cond
    #gradient wrt inp
    ##np.where(condition, value_if_true, value_if_false)
    grad_x = np.where(mask, grad_output, alpha * grad_output)
    # gradient wrt alpha: sum of grad_output * x where x <= 0
    grad_alpha = np.sum(grad_output * x * (~mask))
    return grad_x, float(grad_alpha)

    