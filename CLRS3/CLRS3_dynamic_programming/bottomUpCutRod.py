from math import inf


def bottom_up_cut_rod(prices, length):
    saved_vals = [0 for i in range(length + 1)]
    for j in range(length):
        q = -inf
        for i in range(j+1):
            q = max(q, prices[i] + saved_vals[j - i])
            # argument of saved_vals as 1-based index
            # (j+1)-(i+1)
        saved_vals[j + 1] = q  # adjust for 1-based indexing
    return saved_vals[length]


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print([(i, bottom_up_cut_rod(p, i)) for i in range(1, 11)])


