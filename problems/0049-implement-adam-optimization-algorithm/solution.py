import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    # Note: `f` is accepted only for interface parity with the PyTorch/Tinygrad
    # variants, which derive gradients from it via autograd. This version uses
    # `grad` only — the objective value `f` is never evaluated.
    # Your code here
    #initialize variables
    t = 0
    parameters = x0
    #first and second moment vectors
    mt = 0
    vt = 0
    #hyperpars are given
    bias_m = 0
    bias_v = 0
    #while not converged
    while t < num_iterations:
        #incr time
        t += 1
        #compute gradient
        gt = grad(parameters)
        #update biased 1ste, sec moments
        mt = beta1 * mt + (1 - beta1) * gt
        vt = beta2 * vt + (1 - beta2) * (gt**2)

        #compute biased corrected for 1st en 2nd moments estimate
        bias_m = mt / (1 - (beta1**t))
        bias_v = vt / (1 - (beta2**t))

        #update pars 
        parameters = parameters - learning_rate * (bias_m / ((bias_v**(1/2)) + epsilon))

    return parameters



