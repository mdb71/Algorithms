from math import inf
import numpy as np


def recursive_matrix_chain_1(p, i, j):
    if i == j:
        return 0
    m = np.zeros((len(p)-1, len(p)-1))
    m[i-1, j-1] = inf
    for k in range(i, j):
        q = recursive_matrix_chain_1(p, i, k) + recursive_matrix_chain_1(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if q < m[i - 1, j - 1]:
            m[i - 1, j - 1] = q
    return m.astype(np.int64)[i - 1, j - 1]


def recursive_matrix_chain_2(p, i, j):
    if i == j:
        return 0
    tmp = inf
    for k in range(i, j):
        q = recursive_matrix_chain_2(p, i, k) + recursive_matrix_chain_2(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if q < tmp:
            tmp = q
    return tmp


if __name__ == '__main__':
    dim_seq = [30, 35, 15, 5, 10, 20, 25]
    print(recursive_matrix_chain_1(dim_seq, 1, 6))
    print('\n')
    print(recursive_matrix_chain_2(dim_seq, 1, 6))
