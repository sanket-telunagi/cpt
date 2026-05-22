# Solution for 33. Search in Rotated Sorted Array
# Platform: LeetCode
# Date: 2026-05-22
#

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num == target:
                return idx
        return -1
