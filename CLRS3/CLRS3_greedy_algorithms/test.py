def reverse_func(data):
    i, j = 0, -1
    while i <= len(data) + j:
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    from random import randrange
    from copy import copy

    test_data = [randrange(1, 100) for _ in range(10)]
    print(test_data)
    test_dcp = copy(test_data)
    test_dcp.reverse()
    reverse_func(test_data)
    print(test_dcp, test_data, sep='\n')
