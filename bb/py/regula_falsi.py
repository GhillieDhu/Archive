def find_root(func, a, b, tol):
    aF = func(a)
    bF = func(b)
    if (abs(b - a) < tol):
        return round(max(a, b) / tol) * tol
    elif (aF == 0):
        return a
    elif (bF == 0):
        return b
    else:
        c = (bF * a - aF * b) / (bF - aF)
        cF = func(c)
        if (cF * aF > 0):
            if (abs(c - a) < tol):
                return c
            else:
                return find_root(func, c, b, tol)
        else:
            if (abs(b - c) < tol):
                return c
            else:
                return find_root(func, a, c, tol)
