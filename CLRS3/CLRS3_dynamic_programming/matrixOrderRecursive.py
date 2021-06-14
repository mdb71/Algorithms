from math import inf


def min_cost(p, i, j):      # i, j correspond to 1-based indices 1,2,...,n of p.
    if j < i:
        return None         # checks for malicious input
    if i == j:
        return 0
    q = inf
    for k in range(i, j):
        q = min(q, min_cost(p, i, k) + min_cost(p, k+1, j) + p[i-1]*p[k]*p[j])
    return q


if __name__ == '__main__':
    p = [5, 10, 3, 12, 5, 50, 6]
    print(min_cost(p, 1, len(p)-1))
    # recall that p is one element longer - from 0 to n - than the sequence of matrices -
    # from 1 to n
