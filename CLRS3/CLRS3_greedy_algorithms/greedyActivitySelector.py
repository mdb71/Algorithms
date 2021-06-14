def greedy_activity_selector(s, f):
    n = len(s)
    s = [None] + s
    f = [0] + f         # it's better to use 1- based indexing to improve output readability
    a = [1]
    k = 1
    for m in range(1, n+1):
        if s[m] >= f[k]:
            a += [m]
            k = m
    return a


if __name__ == '__main__':
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(greedy_activity_selector(start_times, finish_times))


