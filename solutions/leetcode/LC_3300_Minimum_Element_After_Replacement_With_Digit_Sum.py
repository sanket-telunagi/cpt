# Solution for 3300. Minimum Element After Replacement With Digit Sum
# Platform: LeetCode
# Date: 2026-05-29
#

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10_000
        for num in nums:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            ans = min(res, ans)
        return ans
