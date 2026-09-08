import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    #standarize data: per feature across samples, mean 0 std 1
    mean = np.mean(data, axis=0) #cols wise aka per feature across all samples
    std = np.std(data, axis=0)

    #apply transformation
    std_data = (data - mean) / std

    #covariance matrix
    cov_matrix = np.cov(std_data, rowvar=False) #rowvar ensures that cols reps features

    #eigenvalues and correspandant eigenvectors => 2 np arrays
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    #sort the eigenvalues -> return idx sorted from largest to smallest
    sorted_eigvals = np.argsort(eigenvalues)[::-1]

    #selecting the corresponding largest eigenvectors per col idx
    sorted_eigenvecs = eigenvectors[:, sorted_eigvals]

    #getting top k  components
    top_k_vectors = sorted_eigenvecs[:, :k]

    #find non zero elem en flip sign
    for i in range(k):
        col = top_k_vectors [:, i] #extrac 1D col
        #find idx of first non zero entry
        idx = np.nonzero(col)[0][0]

        #check if that entry is negative in current col
        if col[idx] < 0:
            #flip the entire sign
            top_k_vectors[:, i] = -col

    return np.round(top_k_vectors, 4)




