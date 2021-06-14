"""Give an O(nlgn)-time algorithm to find the longest monotonically increasing
   subsequence of a sequence of n numbers. (Hint: Observe that the last element of a candidate subsequence
   of length i is at least as large as the last element of a candidate subsequence of length
   i - 1. Maintain candidate subsequences by linking them through the input sequence.)"""

from random import randint
import  numpy as np


def find_lmi_subsequence(x):
    n = len(x)
    c = [1 for i in range(n)]
    b = np.array([[None for i in range(n)] for j in range(n)])
    b[0][0] = 0
    for j in range(1, n):
        i = j - 1
        while i >= 0:
            if x[j] >= x[i]:
                q = c[i] + 1
                if q > c[j]:
                    c[j] = q
                    b[j] = b[i]
            i -= 1
        b[j][j] = j

    def index_subsequence(idx):
        lst = list(b[idx])
        while None in lst:
            lst.remove(None)
        return lst

    return c, b, index_subsequence


if __name__ == '__main__':
    seq = [4, 2, 3, 1]
    seq2 = [randint(1, 50) for i in range(10)]
    seq4 = [9, 17, 22, 2, 50, 32, 6, 43, 30, 33]
    seq5 = [9, 17, 22, 2, 50, 32, 6, 43, 30, 33]
    seq3 = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

    #####################################
    print(seq2, end='\n\n')
    c, b, func = find_lmi_subsequence(seq2)
    print(c)
    # print(func(len(seq4)-3))
    index_list = func(len(seq2)-3)
    print([seq2[i] for i in index_list])
