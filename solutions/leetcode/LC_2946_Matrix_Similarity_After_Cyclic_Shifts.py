# Solution for 2946. Matrix Similarity After Cyclic Shifts
# Platform: LeetCode
# Date: 2026-03-27
#
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        res = [[0] * len(mat[0]) for i in range(len(mat))]
        # n = len()
        for i in range(len(mat)):
            row = mat[i]
            if i % 2 == 0:
                for j in range(len(row)):
                    # use negative indexing of python
                    shifti = (j - k) % len(row)
                    res[i][shifti] = row[j]
            else:
                for j in range(len(row)):
                    shifti = (j + k) % len(row)
                    res[i][shifti] = row[j]

        return res == mat
