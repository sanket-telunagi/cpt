# Solution for 3783. Mirror Distance of an Integer
# Platform: LeetCode
# Date: 2026-04-18
#


class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))
