# Solution for 2906. Construct Product Matrix
# Platform: LeetCode
# Date: 2026-03-24
#
from typing import List


# for each value while going forward we can compute the prefix product by keeping initial value 1, hence every value will be the product of all the previous values
# later use the same approach while traversing reverse, the running product will be the after product the mutual product will give the required answer
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345

        pref = 1
        res = [[0] * len(grid[0]) for j in range(len(grid))]
        # print(res)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i, j)
                res[i][j] = pref
                pref = (pref * grid[i][j]) % MOD

        after = 1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                res[i][j] = (res[i][j] * after) % MOD
                after = (after * grid[i][j]) % MOD

        return res
