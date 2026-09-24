# Solution for 3550 Smallest Index with digit sum equal to Index
# Platform: LeetCode
# Date: 2026-09-24
#

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        n = len(nums)
        for i in range(n):
            if digitSum(nums[i]) == i:
                return i

        return -1


class Solution2:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        for i, num in enumerate(nums):
            if digitSum(num) == i:
                return i

        return -1


class Solution3:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        res = 10000
        for i, num in enumerate(nums):
            if digitSum(num) == i:
                res = min(res, i)

        return -1 if res == 10000 else res
