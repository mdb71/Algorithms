from maxHeapify import left_ch, right_ch


def max_heapify(arr, i):
    arr = [None] + arr
    i +=1
    l = left_ch(i)
    r = right_ch(i)
    largest = 0
    while l <= len(arr) - 1:
        if (l <= len(arr) - 1) and (arr[l] > arr[i]):
            largest = l
        else:
            largest = i

        if (r <= len(arr) - 1) and (arr[r] > arr[largest]):
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, largest)

        i = largest
        l = left_ch(i)
        r = right_ch(i)

    return arr


if __name__ == '__main__':
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print((max_heapify(arr=arr, i=1)))
