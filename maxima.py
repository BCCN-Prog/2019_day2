def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    up = False
    down = False
    for i in range(len(x)):
        if i == 0 or x[i-1] < x[i]:
            up = True
        elif x[i-1] > x[i]:
            up = False

        # if x[i-1] == x[i], no change

        if i+1 == len(x) or x[i+1] < x[i]:
            down = True
        elif x[i+1] > x[i]:
            down = False

        if up and down:
            idx.append(i)

    return idx
