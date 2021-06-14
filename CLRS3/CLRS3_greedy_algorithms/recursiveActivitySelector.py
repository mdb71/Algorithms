def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


if __name__ == '__main__':
    start_times = [None] + [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [0] + [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(recursive_activity_selector(start_times, finish_times, 0, len(finish_times) - 1))
