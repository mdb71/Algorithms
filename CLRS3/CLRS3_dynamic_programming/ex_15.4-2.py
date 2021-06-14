import numpy as np


def lcs_length_2(x, y):
    m, n = len(x), len(y)
    c = np.zeros((m+1, n+1), dtype=np.int64)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i, j] = c[i-1, j-1] + 1
            elif c[i-1, j] >= c[i, j-1]:
                c[i, j] = c[i-1, j]
            else:
                c[i, j] = c[i, j-1]

    # Defaults are only used at the first call. Recursive calls explicitly pass different values to these
    # parameters.

    def print_lcs_2(c, x, i=m, j=n):
        if i == 0 or j == 0:
            return
        if c[i-1, j-1] >= c[i-1, j] and c[i-1, j-1] >= c[i, j-1]:
            print_lcs_2(c, x, i-1, j-1)
        elif c[i-1, j] >= c[i, j-1]:
            print_lcs_2(c, x, i-1, j)
        else:
            print_lcs_2(c, x, i, j-1)

    return c, print_lcs_2


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"
    c, print_lcs_2 = lcs_length_2(x=x, y=y)
    print_lcs_2()