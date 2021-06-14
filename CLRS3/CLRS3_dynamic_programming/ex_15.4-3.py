import numpy as np
from math import inf


def lcs_length_memoized(x, y):
    m = len(x)
    n = len(y)
    c = np.array([[-inf for j in range(n + 1)] for i in range(m + 1)])
    for i in range(1, m+1):
        for j in range(n+1):
          c[i, j] = find_lcs2(x, y, c, i, j)
    return c


# recursive subroutine to find the LCS od two given subsequences

# def find_lcs2(x, y, c, i, j):
#     if i == 1 and j == 1:
#         if x[i-1] == y[j-1]:
#             return 1
#         else:
#             return 0
#     if i == 0 or j == 0:
#         return 0
#     if c[i, j] >= 0:
#         return c[i, j]
#     if x[i-1] == y[j-1]:
#         c[i, j] = find_lcs2(x, y, c,  i-1, j-1) + 1
#     else:
#         return max(find_lcs2(x, y, c,  i-1, j), find_lcs2(x, y, c,  i, j-1))


def find_lcs2(x, y, c, i, j):
    if i == 0 or j == 0:
        return 0
    if i == 1 and j == 1:
        if x[i - 1] == y[j - 1]:
            return 1
        else:
            return 0
    if c[i, j] >= 0:
        return c[i, j]
    if x[i - 1] == y[j - 1]:
        return find_lcs2(x, y, c, i - 1, j - 1) + 1
    else:
        return max(find_lcs2(x, y, c,  i - 1, j), find_lcs2(x, y, c,  i, j - 1))



if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"
    print(lcs_length_memoized(x, y))
