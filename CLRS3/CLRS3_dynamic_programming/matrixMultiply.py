import numpy as np


def matrix_multiply(a, b):
    if a.shape[1] != b.shape[0]:
        return "Error: incompatible dimensions"
    a_rows, a_cols = a.shape[0], a.shape[1]
    b_rows, b_cols = b.shape[0], b.shape[1]
    c = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a_rows):
        for j in range(b_cols):
            # c[i][j] = 0. already set
            for k in range(a_cols):
                c[i][j] += a[i][k] * b[k][j]
    return c


if __name__ == '__main__':
    from random import uniform

    mat_a = np.array([[uniform(0, 10) for i in range(4)] for j in range(5)])
    mat_b = np.array([[uniform(0, 10) for i in range(3)] for j in range(4)])

    print(matrix_multiply(mat_a, mat_b))
