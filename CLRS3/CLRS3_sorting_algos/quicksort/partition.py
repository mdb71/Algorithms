def partition(arr, p, r):  # 0-based indexes
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i+1]
    return i+1


if __name__ == "__main__":
    lst = [2, 8, 7, 1, 3, 5, 6, 4]
    print(partition(arr=lst, p=0, r=len(lst)-1))
