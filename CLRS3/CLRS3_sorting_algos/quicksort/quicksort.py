from partition import partition


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)
    return arr


if __name__ == "__main__":
    lst = [2, 8, 7, 1, 3, 5, 6, 4]
    print(quicksort(arr=lst, p=0, r=len(lst)-1))
