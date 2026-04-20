# Solution for 2078. Two Furthest Houses With Different Colors
# Platform: LeetCode
# Date: 2026-04-20
#

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        for idx, num in enumerate(colors):
            if num != colors[0]:
                res = max(res, idx)

        for idx, num in enumerate(reversed(colors)):
            if num != colors[0]:
                res = max(res, idx)

        return res
