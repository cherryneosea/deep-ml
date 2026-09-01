def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]]:
    rowA = len(a)
    colA = len(a[0])
    
    rowB = len(b)
    colB = len(b[0])

    c = []

    if colA != rowB:
        return -1
    else:
        for row in range(rowA):
            e = []
            for col in range(colB):
                s = 0
                # compute dot-product for each elem
                for k in range(colA):
                    prod = a[row][k] * b[k][col]
                    s += prod
                e.append(s)
            c.append(e)
        return c