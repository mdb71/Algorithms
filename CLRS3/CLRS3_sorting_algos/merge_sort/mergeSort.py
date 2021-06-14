from merge import *


def merge_sort(A , p, r):

    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

    return A


if __name__ == '__main__':
    arr = [2, 4, 5, 7, 1, 2, 3, 6]
    print(merge_sort(arr, 0, 7))


