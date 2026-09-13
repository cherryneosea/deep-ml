import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    #full batch_size gradient_descent
    num_samples = X.shape[0] #returns num of rows
    xt = np.transpose(X)


    if method == 'batch':

        for epoch in range(n_epochs):
            #update weights after seeing all samples at once
            #X.weights
            predictions = np.dot(X, weights)
            #transpose x to match dims when computing gradient 
            grad = np.dot(xt, np.subtract(predictions, y)) * (2 / num_samples)
            #update weights
            weights -= learning_rate * grad



    elif method == 'stochastic':
        #update for each sample individually
        for epoch in range(n_epochs):
            for m in range(num_samples):
                preds = np.dot(X[m], weights)
                error = np.subtract(preds, y[m])
                grad = 2 * error * X[m]
                weights -= learning_rate * grad

    

    #mini batch
    else:
        for epoch in range(n_epochs):
            for i in range(0, num_samples, batch_size):
                sliced_X = X[i:i+batch_size]
                sliced_y = y[i:i+batch_size]
                
                pred = np.dot(sliced_X, weights)
                error = np.subtract(pred, sliced_y)
                
                gradient = (2 / batch_size) * np.dot(sliced_X.T, error)
                weights -= learning_rate * gradient

    return weights




    
