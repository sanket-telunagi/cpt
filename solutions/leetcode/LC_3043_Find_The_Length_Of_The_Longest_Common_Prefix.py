# Solution for 3043. Find the Length of the Longest Common Prefix
# Platform: LeetCode
# Date: 2026-05-21
#

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1.sort()
        arr2.sort()
        hash = set(arr1)
        for num in arr1:
            while num > 0:
                hash.add(num)
                num //= 10

        def getDigits(num):
            res = 0
            while num > 0:
                num //= 10
                res += 1
            return res

        res = 0
        for num in arr2:
            # print(getDigits(num))
            while num > 0:
                if num in hash:
                    res = max(res, getDigits(num))
                num //= 10

        return res
