from math import inf


def merge(A, p, q, r):    # both left and right indices included in the slice

    left = [None for m in range(len(A[p:q+1]))] + [inf] # from p to q with q-p+1 values + inf
    right = [None for m in range(len(A[q+1:r+1]))] + [inf]   # from q+1 to r with r-q values

    for j in range(len(A[p:q+1])):    # i from 0 to q-p takes q-p+1 values
        left[j] = A[j+p]
    for j in range(len(A[q+1:r+1])):    # j from 0 to r-q-1 takes r-q values
        right[j] = A[q+1 + j]

    i = 0
    j = 0
    k = p
    # assume that left and right are sorted
    while k <= r:                   # k from p to r with r-p+1  = len(a[p:q+1]) values
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
            k += 1
            continue
        else:
            A[k] = right[j]
            j += 1
            k += 1
        continue

    return A[p:r + 1]

# if the smallest from left is less than the smallest from right
# then the first element of the slice gets overwritten this way
# and we update the left pointer so that it points to the next
# element to compare. Once we hit one of the sentinels after at
# least min(a[p:q+1], a[q+1:r+1]) steps (i.e. len(...) - 1 steps
# plus the last step which moves the pointer to inf), this sentinel
# causes the elements in the remaining list to be copied.
# Once we have copied all elements we have performed r-p+1 steps.
# Each value of k (k takes r-p+1 values) we copy one element to A.
# Moreover, each value of k corresponds to an increase by one of either
# the left pointer i or right pointer j. So at this stage, one of them is on the sentinel
# and the last value of the A slice has been copied. As the other pointer moves
# onto the other sentinel k increases by one and holds r + 1, going out of range
# and preventing the program from executing the while loop again and thus preventing
# comparison of the two sentinels or indeed that the program attempts to copy one of them
# to an out of range index of the slice A[p:r+1].


if __name__ == '__main__':
    arr = [2, 4, 5, 7, 1, 2, 3, 6]
    print(merge(A=arr, p=0, q=3, r=7))  # NB: q idx included in left
    arr2 = [1]
    print(merge(arr2, 0, 0, 0))
