import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    #create arr of indices en shuffle
    indices = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(indices)

    base_size = n_samples // k 
    remainder = n_samples % k 
    res = []

    #for each fold k 
    for i in range(k):
        #calc slicing indx 
        start = i * base_size + min(i, remainder)
        fold_size = base_size + (1 if i < remainder else 0)
        end = start + fold_size

        #slicing 
        test_idx = indices[start:end].tolist()
        train_indices = np.concatenate([indices[:start], indices[end:]]).tolist()
        #add
        res.append((train_indices, test_idx))

        

    return res 
