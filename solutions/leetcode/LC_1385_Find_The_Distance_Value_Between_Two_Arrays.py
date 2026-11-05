# Solution for 1385. Find the Distance Value Between Two Arrays
# Platform: LeetCode
# Date: 2026-11-05
#


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                res += 1
        return res
