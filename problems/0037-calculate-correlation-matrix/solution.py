import numpy as np

def calculate_correlation_matrix(X, Y=None):
    if Y is None:
        Y = X

    n_features_x = X.shape[1]
    n_features_y = Y.shape[1]

    correlation_matrix = np.zeros((n_features_x, n_features_y))

    for i in range(n_features_x):
        for j in range(n_features_y):
            x_col = X[:, i] # include all rows per feature i
            y_col = Y[:, j]

            mean_x = np.mean(x_col)
            mean_y = np.mean(y_col)
            #compute the pearson correlation for that pair of features
            cov = np.mean((x_col - mean_x) * (y_col - mean_y))
            std_x = np.std(x_col)
            std_y = np.std(y_col)

            correlation_matrix[i, j] = cov / (std_x * std_y)

    return correlation_matrix