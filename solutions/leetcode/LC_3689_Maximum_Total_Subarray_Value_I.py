# Solution for 3689. Maximum Total Subarray Value I
# Platform: LeetCode
# Date: 2026-06-09
#
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k
