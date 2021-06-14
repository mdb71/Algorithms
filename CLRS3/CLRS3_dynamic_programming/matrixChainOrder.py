from math import inf
import numpy as np

"""bottom-up approach"""

""" {n: chain_len, m: min_vals, s: split_pos, l: subchain_len}"""


def matrix_chain_order(p):
    n = len(p) - 1
    m = np.zeros((n, n))
    s = np.zeros((n, n), dtype=np.int64)
    for l in range(2, n + 1):
        for i in range(1, (n - l + 1) + 1):
            j = i + l - 1
            m[i - 1][j - 1] = inf  # initializer // adjust for 0-based indexing: (i,j) --> (i-1,j-1)
            for k in range(i, j):  # index sub-problems // up to and including j-1
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]  # m[(k+1)-1][j-1]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k
    return m.astype(dtype=np.int64), s


def print_optimal_parens(s, i, j):
    if i == j:
        print("A_{}".format(i), end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i-1, j-1])
        print_optimal_parens(s, s[i-1, j-1] + 1, j)
        print(")", end='')


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    print(matrix_chain_order(p)[0])
    print('\n')
    p2 = [5, 10, 3, 12, 5, 50, 6]
    print(matrix_chain_order(p2)[0][0, 5])
    # this tests the recursive version min_cost from matrixOrderRecursive.py as correct

    print('\n')
    s = matrix_chain_order(p)[1]
    print_optimal_parens(s=s, i=1, j=6)
