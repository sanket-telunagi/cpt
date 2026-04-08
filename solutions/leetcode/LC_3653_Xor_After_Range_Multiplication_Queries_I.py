# Solution for 3653. XOR After Range Multiplication Queries I
# Platform: LeetCode
# Date: 2026-04-08
#

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        res = 0
        MOD = 10**9 + 7

        for query in queries:
            l, r, k, v = query
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        for num in nums:
            res ^= num

        return res
