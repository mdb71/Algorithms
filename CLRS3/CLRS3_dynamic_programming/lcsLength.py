import numpy as np


def lcs_length(x, y):
    m, n = len(x), len(y)
    c = np.zeros((m+1, n+1), dtype=np.int64)
    b = np.array([["" for i in range(n)] for i in range(m)], dtype="U2")
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i, j] = c[i-1, j-1] + 1
                b[i-1, j-1] = "nw"
            elif c[i-1, j] >= c[i, j-1]:
                c[i, j] = c[i-1, j]
                b[i-1, j-1] = "u"
            else:
                c[i, j] = c[i, j-1]
                b[i-1, j-1] = "l"
    table = np.array([[{c[i+1, j+1], b[i, j]} for j in range(n)] for i in range(m)])

    def print_lcs(arrows=b, seq=x, i=m, j=n):
        if i == 0 or j == 0:
            return
        if arrows[i - 1, j - 1] == "nw":
            print_lcs(arrows, seq, i - 1, j - 1)
            print(seq[i - 1])
        elif arrows[i-1, j-1] == "u":
            print_lcs(arrows, seq, i - 1, j)
        else:
            print_lcs(arrows, seq, i, j - 1)

    return c, b, table, print_lcs


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"
    print(lcs_length(x, y)[0])
    c, b, table, print_lcs = lcs_length(x, y)
    print_lcs()
