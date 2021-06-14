from math import inf


def find_max_crossing_subarray(A, low, mid, high):

    left_sum = -inf  # this is needed to enter the if loop the first time
    rec_sum = 0     # recursive sum
    max_left = 0
    # as soon as the addition of one further element decreases the sum so far, we stop updating
    # left_sum. NB: this is checked before we enter the if-statement body, thus leaving left_sum at
    # its max value (left_sum trails behind sum by the addition of one element).

    # the left inequality isn't strict: it includes the case where i = min
    i = mid
    while i >= low:
        # initialises rec_sum since the left list contains at least A[mid]
        rec_sum += A[i]
        if rec_sum > left_sum:
            left_sum = rec_sum
            max_left = i          # If next iteration doesn't work, this is retained.
            i -= 1           # initialises i for next iteration
        else:
            i -= 1
            continue

    right_sum = - inf
    rec_sum = 0
    max_right = 0

    j = mid + 1
    while j <= high:
        rec_sum += A[j]
        if rec_sum > right_sum:
            right_sum = rec_sum
            max_right = j
            j += 1
        else:
            j += 1
            continue

    return max_left, max_right, left_sum + right_sum


# test
if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_crossing_subarray(arr, 0, 7, 15))
