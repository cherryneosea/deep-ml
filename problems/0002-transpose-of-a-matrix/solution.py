def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    #rows will be cols, aka num of elemes per list
    rows = len(a)
    cols = len(a[0])
    #init new matrix b with swapped dim
    b = []
    for j in range(cols):
       new_row = []
       for i in range(rows):
            new_row.append(a[i][j])
       b.append(new_row)
    return b

