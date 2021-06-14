from math import inf
import pandas as pd


def extended_bottom_up_cut_rod(prices, length):
    saved_vals = [0 for i in range(length + 1)]
    cuts = [0 for i in range(length + 1)]
    for j in range(length):
        q = -inf
        for i in range(j + 1):
            if q < prices[i] + saved_vals[j - i]:
                q = prices[i] + saved_vals[j - i]
                cuts[j + 1] = i + 1
        saved_vals[j + 1] = q
    return pd.DataFrame(index=pd.RangeIndex(start=0, stop=length+1, step=1), data=zip(saved_vals, cuts),
                        columns=['saved_vals', 'cuts']).T


def print_cut_rod_solution(prices, length):
    saved_vals, cuts = extended_bottom_up_cut_rod(prices, length).T.saved_vals,\
                        extended_bottom_up_cut_rod(prices, length).T.cuts
    idx = length
    while idx > 0:
        print(cuts.loc[idx])
        idx -= cuts.loc[idx]


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(extended_bottom_up_cut_rod(p, 10))
    print('\n')
    print_cut_rod_solution(p, 7)
