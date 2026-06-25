# Solution for 3737. Count Subarrays With Majority Element I
# Platform: LeetCode
# Date: 2026-06-25
#
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            ct = 0
            for j in range(i, n):
                ct += 1 if nums[j] == target else -1
                if ct > 0:
                    res += 1
        return res
