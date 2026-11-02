# Solution for 462. Minimum Moves to Equal Array Elements II
# Platform: LeetCode
# Date: 2026-11-02
#


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        import statistics
        import math
        median = math.floor(statistics.median(nums))
        res = 0 
        for num in nums : 
            res += abs(num - median)
        return res
