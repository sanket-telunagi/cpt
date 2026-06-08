# Solution for 2161. Partition Array According to Given Pivot
# Platform: LeetCode
# Date: 2026-06-08
#
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a1, a2, a3 = [], [], []

        for num in nums:
            if num < pivot:
                a1.append(num)
            elif num == pivot:
                a2.append(num)
            else:
                a3.append(num)

        return a1 + a2 + a3
