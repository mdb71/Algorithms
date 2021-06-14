from math import inf


def memoized_cut_rod_aux(prices, length, saved_vals):
    if saved_vals[length] >= 0:
        return saved_vals[length]
    if length == 0:
        q = 0
    else:
        q = -inf
        for i in range(length):
            q = max(q, prices[i] + memoized_cut_rod_aux(prices, length-(i+1), saved_vals))
    saved_vals[length] = q
    return q


def memoized_cut_rod(prices, length):
    r = [-inf for i in range(length+1)]
    return memoized_cut_rod_aux(prices, length, saved_vals=r)


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print([(i, memoized_cut_rod(p, i)) for i in range(1, 11)])
