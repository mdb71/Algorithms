def parent(i):
    return i // 2


def left_ch(i):
    return 2 * i


def right_ch(i):
    return 2 * i + 1


def max_heapify(arr, i, size):  # pass i by 1-based
    one_to_zero = {j + 1: j for j in range(size)}
    # zero_to_one = {value:key for key, value in zip(one_to_zero.keys(), one_to_zero.values())}
    l = left_ch(i)
    r = right_ch(i)

    if (l <= size) and (arr[one_to_zero[l]] > arr[one_to_zero[i]]):
        largest = l
    else:
        largest = i

    if (r <= size) and (arr[one_to_zero[r]] > arr[one_to_zero[largest]]):
        largest = r

    if largest != i:
        arr[one_to_zero[i]], arr[one_to_zero[largest]] = arr[one_to_zero[largest]], \
                                                         arr[one_to_zero[i]]
        return max_heapify(arr, largest, size=size)
    else:
        return arr


if __name__ == '__main__':
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(max_heapify(arr=arr, i=2, size=len(arr)))  # second element in 1-based indexing
    print(arr)
