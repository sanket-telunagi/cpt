# Solution for 453. Minimum Moves to Equal Array Elements
# Platform: LeetCode
# Date: 2026-11-01
#
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


class Solution2:
    def minMoves(self, nums: list[int]) -> int:
        min_x = min(nums)
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res += nums[i] - min_x
        return res
