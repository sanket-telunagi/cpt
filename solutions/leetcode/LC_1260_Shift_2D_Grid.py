# Solution for 1260 Shift 2D grid
# Platform: LeetCode
# Date: 2026-07-20
#
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flat = []
        for nums in grid:
            for num in nums:
                flat.append(num)

        m = len(grid)
        n = len(grid[0])

        for i in range(k):
            first = flat.pop()
            flat.insert(0, first)

        start = 0
        res = []

        for i in range(m):
            res.append(flat[start : start + n])
            start += n

        return res
