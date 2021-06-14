from math import inf
import numpy as np


def lookup_chain(m, p, i, j):
    if m[i-1, j-1] < inf:
        return m[i-1, j-1]
    if i == j:
        return 0
    for k in range(i, j):
        q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i-1]*p[k]*p[j]
        if q < m[i-1, j-1]:
            m[i-1, j-1] = q
    return m.astype(np.int64)[i-1, j-1]


def memoized_matrix_chain(p):
    n = len(p) -1
    m = np.array([[inf for i in range(n)] for j in range(n)])
    return lookup_chain(m, p, 1, n)


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    print(memoized_matrix_chain(p=p))
