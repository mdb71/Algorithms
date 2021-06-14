from math import inf
import pandas as pd


def optimal_bst(p, q, n):
    if sum(p) + sum(q) != 1:
        return "Invalid Data Error"

    data_e = {i: [0 for r in range(n + 1)] for i in range(n + 1)}
    data_root = {i: [0 for r in range(n)] for i in range(n)}
    data_w = {i: [0 for r in range(n)] for i in range(n)}

    p = pd.Series(data=p, index=pd.RangeIndex(1, n + 1))
    q = pd.Series(data=q, index=pd.RangeIndex(0, n + 1))
    e = pd.DataFrame(data=data_e, index=pd.RangeIndex(1, n + 2),
                     columns=pd.RangeIndex(0, n + 1))
    root = pd.DataFrame(data=data_root, index=pd.RangeIndex(1, n + 1),
                        columns=pd.RangeIndex(1, n + 1))
    w = pd.DataFrame(data=data_w, index=pd.RangeIndex(1, n + 1),
                     columns=pd.RangeIndex(1, n + 1))

    for i in range(1, n + 2):
        e.loc[i, i - 1] = q.loc[i - 1]
        w.loc[i, i - 1] = q.loc[i - 1]

    for l in range(1, n + 1):
        for i in range(1, (n - l + 1) + 1):
            j = i + l - 1
            e.loc[i, j] = inf
            w.loc[i, j] = w.loc[i, j - 1] + p.loc[j] + q.loc[j]
            for r in range(i, j + 1):
                t = e.loc[i, r - 1] + e.loc[r + 1, j] + w.loc[i, j]
                if t < e.loc[i, j]:
                    e.loc[i, j] = t
                    root.loc[i, j] = r

    return e, root


if __name__ == '__main__':
    p = [0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    n = len(p)
    for i in range(2):
        print(optimal_bst(p, q, n)[i], end='\n\n')
