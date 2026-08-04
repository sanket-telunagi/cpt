# Solution for 3731 Find Missing Elements
# Platform: LeetCode
# Date: 2026-08-04
#
#
from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx = max(nums)
        lx = min(nums)
        res = []
        for i in range(lx, mx + 1) :
            if i not in nums :
                res.append(i)
        return res
