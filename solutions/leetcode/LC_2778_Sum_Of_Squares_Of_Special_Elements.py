# Solution for 2778. Sum of Squares of Special Elements
# Platform: LeetCode
# Date: 2026-10-11
#


class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:

        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                res += num**2
        return res
