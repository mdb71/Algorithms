from buildMaxHeap import build_max_heap
from maxHeapify import max_heapify, parent
from math import inf


def one_to_zero(i, arr):
    if not 1 <= i <= len(arr):
        raise IndexError
    dic_idx = {j + 1: j for j in range(len(arr))}
    return dic_idx[i]


def heap_maximum(heap):
    return heap[one_to_zero(1, heap)]


def heap_extract_max(heap, size):
    if size < 1:
        return None
    max_val = heap.pop(0)
    heap[one_to_zero(1, heap)], heap[one_to_zero(len(heap), heap)] \
        = heap[one_to_zero(len(heap), heap)], heap[one_to_zero(1, heap)]
    size -= 1
    max_heapify(heap, 1, size=size)
    return max_val


def heap_increase_key(heap, i, key):
    if key < heap[one_to_zero(i, heap)]:
        return "Error: new key is smaller than current key."
    heap[one_to_zero(i, heap)] = key
    while i > 1 and heap[one_to_zero(parent(i), heap)] < heap[one_to_zero(i, heap)]:
        heap[one_to_zero(parent(i), heap)], heap[one_to_zero(i, heap)] \
            = heap[one_to_zero(i, heap)], heap[one_to_zero(parent(i), heap)]
        i = parent(i)
    return heap


def max_heap_insert(heap, key):
    heap.append(-inf)
    heap_increase_key(heap, len(heap), key)
    return heap


if __name__ == '__main__':
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heap_extract_max(build_max_heap(arr), size=len(arr)))
    print(arr)      # checks that change is in place
    print('\n')

    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heap_increase_key(build_max_heap(arr), 6, 25))
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(build_max_heap(arr=heap_increase_key(build_max_heap(arr), 6, 25))) # checks that it returns a heap
    print('\n')

    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(max_heap_insert(build_max_heap(arr), 13))
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(build_max_heap(max_heap_insert(build_max_heap(arr), 13)))    # checks it returns a heap
