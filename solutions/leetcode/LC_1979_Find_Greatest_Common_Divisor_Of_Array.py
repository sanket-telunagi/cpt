# Solution for 1979 Find Greatest Common Divisor of Array
# Platform: LeetCode
# Date: 2026-07-18
#
#
from math import gcd, inf
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        low = int(inf)
        hi = -1
        for num in nums:
            low = min(low, num)
            hi = max(hi, num)
        # print(s,l)

        return gcd(low, hi)
