# Solution for 1846. Maximum Element After Decreasing and Rearranging
# Platform: LeetCode
# Date: 2026-06-28
#

from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        arr[0] = 1
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1

        return arr[-1]
