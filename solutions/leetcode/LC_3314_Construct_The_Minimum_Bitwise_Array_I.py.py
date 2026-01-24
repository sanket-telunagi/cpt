# Solution for LC 3314 Construct the minimum bitwise array I
# Platform: LeetCode
# Date: 2026-01-20
#

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def getValue(num):
            for i in range(1, 2001):
                if i | i + 1 == num:
                    return i
            return -1

        res = []
        for num in nums:
            res.append(getValue(num))

        return res
