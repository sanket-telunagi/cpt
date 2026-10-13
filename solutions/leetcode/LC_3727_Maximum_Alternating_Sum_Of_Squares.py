# Solution for 3727. Maximum Alternating Sum of Squares
# Platform: LeetCode
# Date: 2026-10-13
#


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = list(map(abs, nums))
        nums.sort()

        n = len(nums)

        res = 0

        for i in range(n // 2):
            res += nums[n - i - 1] ** 2
            res -= nums[i] ** 2
        if n % 2 != 0:
            res += nums[n // 2] ** 2

        return res
