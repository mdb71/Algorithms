from math import inf


def cut_rod(prices, length):
    if length == 0:
        return 0
    q = - inf
    for i in range(length):
        q = max(q, prices[i] + cut_rod(prices, length - (i + 1)))  # adjust for zero based indexing
    return q


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cut_rod(p, 4))
