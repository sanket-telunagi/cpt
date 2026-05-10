# Solution for 2770. Maximum Number of Jumps to Reach the Last Index
# Platform: LeetCode
# Date: 2026-05-10
#

from functools import cache
from typing import List
from math import inf


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            res = -inf
            for j in range(i + 1, len(nums)):
                if abs(nums[j] - nums[i]) <= target:
                    res = max(res, dfs(j) + 1)
            return res

        ans = dfs(0)
        return -1 if ans < 0 else ans
