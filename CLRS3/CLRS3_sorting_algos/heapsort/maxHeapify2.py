"""Using Pandas to transform to 1-based indexing."""


import pandas as pd
from maxHeapify import left_ch, right_ch


def max_heapify_2(series, label):
    l = left_ch(label)
    r = right_ch(label)

    if (l in series.index) and (series.loc[l] > series.loc[label]):
        largest = l
    else:
        largest = label

    if (r in series.index) and (series.loc[r] > series.loc[largest]):
        largest = r

    if largest != label:
        series.loc[label], series.loc[largest] = series.loc[largest], series.loc[label]
        return max_heapify_2(series, largest)
    else:
        return series

def max_heapify_transform(arr, i, zero_based = False):  # pass i as 1-based index
    ser = pd.Series(data = arr, index=pd.RangeIndex(start=1, stop=len(arr)+1))
    if zero_based:
        i += 1

    return max_heapify_2(ser, i).values


if __name__ == '__main__':
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(max_heapify_transform(arr=arr, i=2))  # second element in 0-based indexing

