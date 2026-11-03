# Solution for 3736. Minimum Moves to Equal Array Elements III
# Platform: LeetCode
# Date: 2026-11-03
#


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # return (sum([abs(max(nums) - num) for num in nums]))
        return max(nums) * len(nums) - sum(nums)
        
class Solution2 : 
    def minMoves(self, nums: list[int]) -> int: 
        return (sum([abs(max(nums) - num) for num in nums]))
