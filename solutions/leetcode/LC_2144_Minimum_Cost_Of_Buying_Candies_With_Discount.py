# Solution for 2144. Minimum Cost of Buying Candies With Discount
# Platform: LeetCode
# Date: 2026-06-01
#
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n = len(cost)
        res = 0
        for i in range(n):
            if (i + 1) % 3 == 0:
                continue
            res += cost[i]
        return res
