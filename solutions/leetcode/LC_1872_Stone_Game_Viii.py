# Solution for 1872 Stone Game VIII
# Platform: LeetCode
# Date: 2026-08-24
#
#
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        n = len(stones)
        pre = list(accumulate(stones))

        def solve(i: int) -> int:
            if i == n - 1:
                return pre[n - 1]
            next_val = solve(i + 1)
            return max(next_val, pre[i] - next_val)

        return solve(1)
