from maxHeapify import max_heapify


def build_max_heap(arr):
    i = len(arr) // 2
    while i > 0:
        max_heapify(arr, i, len(arr))
        i -= 1
    return arr


if __name__ == '__main__':
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(build_max_heap(a))
