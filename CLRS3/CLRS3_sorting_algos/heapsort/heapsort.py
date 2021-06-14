from buildMaxHeap import build_max_heap
from maxHeapify import max_heapify


def heapsort(arr):
    one_to_zero = {j + 1: j for j in range(len(arr))}
    build_max_heap(arr)
    i = len(arr)
    while i > 1:
        arr[one_to_zero[1]], arr[one_to_zero[i]] = arr[one_to_zero[i]], arr[one_to_zero[1]]
        i -= 1
        max_heapify(arr, 1, i)
    return arr


if __name__ == '__main__':
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heapsort(a))
